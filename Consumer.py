#!/usr/bin/env python3
import json
import logging
import os
import sys
from urllib.parse import urlparse, unquote
import pika
from dotenv import load_dotenv
from provision.provisioner import Provisioner
import uuid

logging.getLogger("pika").setLevel(logging.ERROR)

# Load env file if present
try:
    load_dotenv("/etc/rabbit-consumer.env")
except Exception:
    pass


def _normalize_from_url():
    
    url = os.getenv("RABBIT_URL")
    
    if not url:
        return

    p = urlparse(url)

    os.environ.setdefault("RABBIT_HOST", p.hostname or "")
    os.environ.setdefault(
        "RABBIT_PORT",
        str(p.port or (5671 if p.scheme == "amqps" else 5672))
    )
    os.environ.setdefault("RABBIT_VHOST", p.path.lstrip("/") or "/")

    if p.username:
        os.environ.setdefault("RABBIT_USER", unquote(p.username))

    if p.password:
        os.environ.setdefault("RABBIT_PASS", unquote(p.password))


_normalize_from_url()


# ---- Config ----
RABBIT_HOST     = os.getenv("RABBIT_HOST")
RABBIT_PORT     = int(os.getenv("RABBIT_PORT"))
RABBIT_VHOST    = os.getenv("RABBIT_VHOST")
RABBIT_USER     = os.getenv("RABBIT_USER")
RABBIT_PASS     = os.getenv("RABBIT_PASS")
QUEUE_NAME      = os.getenv("QUEUE_NAME")
DLX_ENABLED     = True


logging.basicConfig(
    level   = logging.INFO,
    format  = "%(asctime)s %(levelname)s %(message)s",
    stream  = sys.stdout,
)


# Explicit registry of allowed handler classes
CLASS_REGISTRY = {
    "Provisioner": Provisioner,
}


def validate_message(data: dict) -> dict:

    if not isinstance(data, dict):
        raise ValueError("Message must be a JSON object")

    if "Namespace" not in data or not isinstance(data["Namespace"], str):
        raise ValueError("Missing/invalid 'Namespace' (str)")

    if "Action" not in data or not isinstance(data["Action"], str):
        raise ValueError("Missing/invalid 'action' (str)")

    if "UserID" not in data:
        raise ValueError("Missing 'UserID'")

    try:
        data["UserID"] = int(data["UserID"])
    except Exception:
        raise ValueError("'UserID' must be int")

    return data


def get_handler_instance(namespace: str):
    
    cls = CLASS_REGISTRY.get(namespace)
    
    if not cls:
        raise ValueError(f"Unknown Namespace '{namespace}'")
    
    return cls()


def handle_action(handler, action: str, user_id: int, data: dict):
    
    action = action.lower()

    if action == "provision":
        

        return handler.provision(user_id,data['Domain'],str(uuid.uuid4()))


    if action == "ftp":
        logging.info("FTP action requested but not implemented")
        return None

    if action == "dns":
        logging.info("DNS action requested but not implemented")
        return None

    if action == "coolify":
        logging.info("Coolify action requested but not implemented")
        return None

    if action == "proxy":
        logging.info("Proxy action requested but not implemented")
        return None

    if action == "reporting":
        logging.info("Reporting action requested but not implemented")
        return None

    raise ValueError(f"Unknown action '{action}'")


def on_message(ch, method, properties, body):

    try:
        payload = body.decode("utf-8")

        logging.info(f"Received: {payload}")

        data    = json.loads(payload)
        data    = validate_message(data)
        handler = get_handler_instance(data["Namespace"])
        result  = handle_action(
                    handler = handler,
                    action  = data["Action"],
                    user_id = data["UserID"],
                    data    = data["Params"],
                )

        logging.info(
            f"Action '{data['Action']}' for user {data['UserID']} OK. Result: {result}"
        )
        ch.basic_ack(delivery_tag = method.delivery_tag)

    except ValueError as e:

        logging.error(f"Bad message: {e}")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    except Exception as e:
        
        logging.exception(f"Processing failed: {e}")

        if DLX_ENABLED:
            ch.basic_nack(delivery_tag = method.delivery_tag, requeue = False)
        else:
            ch.basic_nack(delivery_tag = method.delivery_tag, requeue = True)


def main():

    logging.info(
        f"Connecting to RabbitMQ host = {RABBIT_HOST} port = {RABBIT_PORT} "
        f"vhost = {RABBIT_VHOST} queue = {QUEUE_NAME}"
    )

    creds   = pika.PlainCredentials(RABBIT_USER, RABBIT_PASS)
    params  = pika.ConnectionParameters(
                        host            = RABBIT_HOST,
                        port            = RABBIT_PORT,
                        virtual_host    = RABBIT_VHOST,
                        credentials     = creds,
                    )

    connection  = pika.BlockingConnection(params)
    channel     = connection.channel()

    channel.queue_declare(queue = QUEUE_NAME, durable = True)
    channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(queue = QUEUE_NAME, on_message_callback = on_message)

    logging.info(f"[*] Waiting for JSON messages on '{QUEUE_NAME}'...")

    try:
        channel.start_consuming()

    except KeyboardInterrupt:

        logging.info("Shutting down...")
        channel.stop_consuming()
        connection.close()


if __name__ == "__main__":
    main()

