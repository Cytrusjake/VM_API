from dotenv import load_dotenv

import os

load_dotenv()


class Config:

    @property
    def agent_name(self):
        return os.getenv("AGENT_NAME")

    @property
    def agent_version(self):
        return os.getenv("AGENT_VERSION")

    @property
    def agent_service(self):
        return os.getenv("AGENT_SERVICE")

    
    @property
    def pika_host(self):
        return os.getenv("PIKA_HOST")

    @property
    def pika_port(self):
        return int(os.getenv("PIKA_PORT", 5672))

    @property
    def pika_username(self):
        return os.getenv("PIKA_USERNAME")

    @property
    def pika_password(self):
        return os.getenv("PIKA_PASSWORD")

    @property
    def pika_queue(self):
        return os.getenv("PIKA_QUEUE")

    @property
    def pika_response_queue(self):
        return os.getenv("PIKA_RESPONSE_QUEUE")

    @property
    def log_level(self):
        return os.getenv("LOG_LEVEL", "INFO")
        