from result import Result


class Router:

    def __init__(self, registry):
        self.registry = registry

    def dispatch(self, message):

        manager = self.registry.get(message.namespace)

        if manager is None:

            return Result.failed_result(
                f"Unknown namespace '{message.namespace}'"
            )

        try:
            return manager.execute(message)

        except Exception as ex:
            return Result.failed_result(ex)

            