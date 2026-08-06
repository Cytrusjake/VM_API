import json
import sys
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

        #
        # Ensure queues exist
        #

        self.channel.queue_declare(
            queue=self.config.pika_queue,
            durable=True
        )

        self.channel.queue_declare(
            queue=self.config.pika_response_queue,
            durable=True
        )

    ####################################################################
    # Publish
    ####################################################################

    def publish(self):

        if len(sys.argv) < 3:

            print()
            print("Usage:")
            print("  python3 test_publish.py <Namespace> <Action>")
            print("  python3 test_publish.py <Namespace> <Action> '<JSON Parameters>'")
            print()
            print("Examples:")
            print("  python3 test_publish.py Resources Hostname")
            print("  python3 test_publish.py Agent Ping")
            print("  python3 test_publish.py Redis FlushAll")
            print('  python3 test_publish.py PHP SetMemory \'{"Memory":"512M"}\'')
            print()

            sys.exit(1)

        namespace = sys.argv[1]
        action = sys.argv[2]

        parameters = {}

        if len(sys.argv) > 3:
            parameters = json.loads(sys.argv[3])

        message = {

            "MessageID": str(uuid.uuid4()),
            "RequestID": str(uuid.uuid4()),

            "Namespace": namespace,
            "Action": action,

            "ReplyTo": self.config.pika_response_queue,

            "Parameters": parameters

        }

        self.channel.basic_publish(

            exchange="",

            routing_key=self.config.pika_queue,

            body=json.dumps(message),

            properties=pika.BasicProperties(

                delivery_mode=2

            )

        )

        print()
        print("============================================================")
        print("MESSAGE PUBLISHED")
        print("============================================================")
        print(json.dumps(message, indent=4))
        print()

    ####################################################################
    # Receive
    ####################################################################

    def receive(self):

        print("Waiting for response...")
        print()

        while True:

            method, properties, body = self.channel.basic_get(

                queue=self.config.pika_response_queue,

                auto_ack=True

            )

            if body:

                print("============================================================")
                print("RESPONSE")
                print("============================================================")
                print(
                    json.dumps(
                        json.loads(body),
                        indent=4
                    )
                )
                print()

                break

    ####################################################################
    # Run
    ####################################################################

    def run(self):

        self.publish()

        self.receive()

        self.connection.close()


if __name__ == "__main__":

    TestPublisher().run()