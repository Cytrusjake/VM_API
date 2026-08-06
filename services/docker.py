from result import Result


class DockerService:

    def __init__(self, shell):
        self.shell = shell

    def ps(self):

        result = self.shell.execute(
            "docker ps --format '{{json .}}'"
        )

        if not result.success:
            return Result.failed_result(result.stderr)

        containers = []

        for line in result.stdout.splitlines():

            if line.strip():
                containers.append(line)

        return Result.success_result(
            data = {
                "containers": containers
            }
        )

    def restart(self, container):

        result = self.shell.execute(
            f"docker restart {container}"
        )

        if not result.success:
            return Result.failed_result(result.stderr)

        return Result.success_result(
            f"Container '{container}' restarted."
        )

    def stop(self, container):

        result = self.shell.execute(
            f"docker stop {container}"
        )

        if not result.success:
            return Result.failed_result(result.stderr)

        return Result.success_result(
            f"Container '{container}' stopped."
        )

    def start(self, container):

        result = self.shell.execute(
            f"docker start {container}"
        )

        if not result.success:
            return Result.failed_result(result.stderr)

        return Result.success_result(
            f"Container '{container}' started."
        )
        