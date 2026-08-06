# managers/base.py

from result import Result


class BaseManager:

    COMMANDS = {}

    def __init__(self, context):
        self.context = context

    def execute(self, message):

        handler = self.COMMANDS.get(message.action)

        if handler is None:

            return Result.failed_result(
                f"Unknown action '{message.action}' "
                f"for namespace '{message.namespace}'"
            )

        return handler(message.parameters)

        