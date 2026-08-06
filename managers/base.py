# managers/base.py

from abc import ABC
from result import Result


class BaseManager(ABC):

    COMMANDS = {}

    def __init__(self, context):
        self.context = context

   
    @property
    def logger(self):
        return self.context.logger

    @property
    def config(self):
        return self.context.config

    @property
    def database(self):
        return self.context.database

    @property
    def services(self):
        return self.context.services

   
    def execute(self, message):

        handler = self.COMMANDS.get(message.action)

        if handler is None:

            return Result.failed_result(
                f"Unknown action '{message.action}' "
                f"for namespace '{message.namespace}'"
            )

        try:

            self.logger.info(
                f"Executing {message.namespace}.{message.action}"
            )

            return handler(message.parameters)

        except Exception as ex:

            self.logger.exception(ex)

            return Result.failed_result(ex)

            