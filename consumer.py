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

            self.logger.command(command)

            result = self.router.dispatch(command)

        except Exception as ex:

            self.logger.command_exception(
                command,
                ex
            )

            result = Result.failed_result(ex)

        finally:

            if result is not None:

                result.duration = round(
                    time.perf_counter() - start,
                    3
                )

                self.logger.result(result)

        return command, result

        