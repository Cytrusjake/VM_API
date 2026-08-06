import json
import uuid

import pika

from config import Config


class TestPublisher:

    def __init__(self):

        self.config = Config()

        credentials = pika.PlainCredentials(
            self.config.pika_username,
            self.config.pika_password
        )

        parameters = pika.ConnectionParameters(
            host=self.config.pika_host,
            port=self.config.pika_port,
            credentials=credentials
        )

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        

        self.channel.queue_declare(
            queue=self.config.pika_response_queue,
            durable=True
        )

    
    def publish(self):

        message = {

            "MessageID": str(uuid.uuid4()),
            "RequestID": str(uuid.uuid4()),
            "Namespace": "Resources",
            "Action": "Hostname",
            "ReplyTo": self.config.pika_response_queue,
            "Parameters": {}

        }

        self.channel.basic_publish(

            exchange = "",
            routing_key = self.config.pika_queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2
            )

        )

        print("Message Published")
        print(json.dumps(message, indent=4))

    
    def receive(self):

        print()
        print("Waiting for response...")
        print()

        method, properties, body = self.channel.basic_get(

            queue=self.config.pika_response_queue,

            auto_ack=True

        )

        while body is None:

            method, properties, body = self.channel.basic_get(

                queue=self.config.pika_response_queue,

                auto_ack=True

            )

        print("Response Received")
        print()

        print(
            json.dumps(
                json.loads(body),
                indent=4
            )
        )

    
    def run(self):

        self.publish()

        self.receive()

        self.connection.close()


if __name__ == "__main__":

    TestPublisher().run()