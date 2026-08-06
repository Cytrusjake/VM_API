from managers.base import BaseManager
from result import Result

import os
import platform
import socket


class SystemManager(BaseManager):

    def __init__(self, context):

        super().__init__(context)

        self.COMMANDS = {
            "Ping"      : self.ping,
            "Hostname"  : self.hostname,
            "Version"   : self.version,
            "Uptime"    : self.uptime
        }

    def ping(self, params):

        return Result.success_result(
            message = "Pong"
        )

    def hostname(self, params):

        return Result.success_result(
            data = {
                "hostname": socket.gethostname()
            }
        )

    def version(self, params):

        return Result.success_result(
            data = {
                "python"    : platform.python_version(),
                "platform"  : platform.platform()
            }
        )

    def uptime(self, params):

        shell   = self.services["shell"]
        output  = shell.execute("uptime")

        if not output.success:
            return Result.failed_result(output.stderr)

        return Result.success_result(
            data = {
                "uptime": output.stdout
            }
        )
        