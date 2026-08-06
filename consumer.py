import time

from message import Message
from result import Result


class Consumer:


    def __init__(self, router, logger):
        self.router = router
        self.logger = logger

    def execute(self, body):

        start   = time.perf_counter()
        command = None
        result  = None

        try:

            command = Message.from_json(body)

            self.logger.info(
                f"[{command.request_id}] "
                f"Received {command.namespace}.{command.action}"
            )

            result = self.router.dispatch(command)

        except Exception as ex:

            self.logger.exception(ex)

            result = Result.failed_result(ex)

        finally:

            if result is not None:
                result.duration = round(
                    time.perf_counter() - start,
                    3
                )

        if command is not None:

            self.logger.info(
                f"[{command.request_id}] "
                f"Completed {command.namespace}.{command.action} "
                f"in {result.duration:.3f}s "
                f"({result.status})"
            )

        else:

            self.logger.error(
                f"Command parsing failed "
                f"({result.duration:.3f}s)"
            )

        return command, result

        