import json
import logging
import sys


class Logger:

    def __init__(self, name = "Consumer"):

        self.logger = logging.getLogger(name)

        if self.logger.handlers:
            return

        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        )

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

   
    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, ex):
        self.logger.exception(ex)

    def command(self, command):

        self.logger.info(
            "\n"
            "============================================================\n"
            "REQUEST\n"
            "============================================================\n"
            f"Request ID    : {command.request_id}\n"
            f"Message ID    : {command.message_id}\n"
            f"Namespace     : {command.namespace}\n"
            f"Action        : {command.action}\n"
            "Parameters     :\n"
            f"{json.dumps(command.parameters, indent = 4)}\n"
            "============================================================"
        )

    
    def result(self, result):

        self.logger.info(
            "\n"
            "============================================================\n"
            "RESULT\n"
            "============================================================\n"
            f"Success       : {result.success}\n"
            f"Status        : {result.status}\n"
            f"Duration      : {result.duration}\n"
            f"Message       : {result.message}\n"
            f"Error         : {result.error}\n"
            f"Hostname      : {result.hostname}\n"
            "Data           :\n"
            f"{json.dumps(result.data, indent = 4, default = str)}\n"
            "============================================================"
        )

   
    def command_exception(self, command, ex):

        self.logger.exception(
            "\n"
            "============================================================\n"
            "EXCEPTION\n"
            "============================================================\n"
            f"Request ID : {command.request_id if command else 'Unknown'}\n"
            f"Message ID : {command.message_id if command else 'Unknown'}\n"
            f"Namespace  : {command.namespace if command else 'Unknown'}\n"
            f"Action     : {command.action if command else 'Unknown'}\n"
            f"Exception  : {ex}\n"
            "============================================================"
        )
