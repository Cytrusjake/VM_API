# pika_client.py


import json
import time
import pika
from response_builder import ResponseBuilder

class PikaClient:

    def __init__(
        self,
        config,
        consumer,
        logger
    ):

        self.config 	= config
        self.consumer 	= consumer
        self.logger 	= logger

        self.connection = None
        self.channel 	= None

    
    def connect(self):

        credentials = pika.PlainCredentials(
            self.config.pika_username,
            self.config.pika_password
        )

        parameters = pika.ConnectionParameters(
            host 		= self.config.pika_host,
            port 		= self.config.pika_port,
            credentials = credentials,
            heartbeat 	= 60,
            blocked_connection_timeout = 300
        )

        self.connection = pika.BlockingConnection(
            parameters
        )

        self.channel = self.connection.channel()

        self.channel.queue_declare(
            queue 	= self.config.pika_queue,
            durable = True
        )

        self.logger.info(
            f"Connected to RabbitMQ "
            f"({self.config.pika_host})"
        )

   
    def disconnect(self):

        if self.connection and self.connection.is_open:

            self.connection.close()
            self.logger.info(
                "Disconnected from RabbitMQ"
            )

    
    def publish(
        self,
        queue,
        message
    ):

        if isinstance(message, dict):

            message = json.dumps(message)

        self.channel.basic_publish(

            exchange 	= "",
            routing_key	= queue,
            body 		= message,
            properties 	= pika.BasicProperties(
              	delivery_mode = 2

            )

        )

    
    def consume(self):

        self.channel.basic_qos(

            prefetch_count = 1

        )

        self.channel.basic_consume(

            queue = self.config.pika_queue,

            on_message_callback = self._callback

        )

        self.logger.info(

            f"Listening on queue "
            f"{self.config.pika_queue}"

        )

        self.channel.start_consuming()

    
    def _callback(

        self,
        channel,
        method,
        properties,
        body

    ):

        command = None

        try:

            command, result = self.consumer.execute(body)

            response = ResponseBuilder.build(
                command,
                result
            )

            reply_queue = (
                command.reply_to
                or
                self.config.pika_response_queue
            )

            self.logger.info(
                f"Published response to '{reply_queue}'"
            )

            channel.basic_ack(
                delivery_tag = method.delivery_tag
            )

            self.logger.info(
                f"Acknowledged message {command.message_id}"
            )

        except Exception as ex:

            self.logger.exception(ex)

            channel.basic_nack(

                delivery_tag 	= method.delivery_tag,
                requeue 		= False

            )

    
    def run(self):

        while True:

            try:
                self.connect()
                self.consume()

            except KeyboardInterrupt:

                self.disconnect()

                break

            except Exception as ex:

                self.logger.exception(ex)
                self.logger.info(
                    "Reconnecting in 5 seconds..."
                )

                time.sleep(5)