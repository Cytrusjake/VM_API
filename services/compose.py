# services/compose.py

from result import Result


class ComposeService:

    def __init__(self, shell):
        self.shell = shell

    
    def _run(self, directory, command):

        shell_result = self.shell.execute(
            command     = command,
            cwd         = directory
        )

        if not shell_result.success:
            return Result.failed_result(shell_result.stderr)

        return Result.success_result(
            data = {
                "stdout": shell_result.stdout,
                "stderr": shell_result.stderr
            }
        )

    
    def deploy(self, directory):
        

        result = self.pull(directory)

        if not result.success:
            return result

        return self.up(directory)

    def pull(self, directory):

        return self._run(
            directory,
            "docker compose pull"
        )

    def up(self, directory, detach=True):

        command = "docker compose up"

        if detach:
            command += " -d"

        return self._run(
            directory,
            command
        )

    def down(self, directory):

        return self._run(
            directory,
            "docker compose down"
        )

    def restart(self, directory):

        return self._run(
            directory,
            "docker compose restart"
        )

    def stop(self, directory):

        return self._run(
            directory,
            "docker compose stop"
        )

    def start(self, directory):

        return self._run(
            directory,
            "docker compose start"
        )

    def build(self, directory):

        return self._run(
            directory,
            "docker compose build"
        )

    def ps(self, directory):

        return self._run(
            directory,
            "docker compose ps"
        )

    def images(self, directory):

        return self._run(
            directory,
            "docker compose images"
        )

    def config(self, directory):

        return self._run(
            directory,
            "docker compose config"
        )

    def validate(self, directory):

        return self._run(
            directory,
            "docker compose config --quiet"
        )

   
    def logs(
        self,
        directory,
        service = None,
        lines   = 100
    ):

        command = f"docker compose logs --tail {lines}"

        if service:
            command += f" {service}"

        return self._run(
            directory,
            command
        )

   
    def update(self, directory):
        
        result = self.pull(directory)

        if not result.success:
            return result

        return self.restart(directory)

    def rebuild(self, directory):
       
        result = self.build(directory)

        if not result.success:
            return result

        return self.up(directory)

   
    def prune_images(self):

        shell_result = self.shell.execute(
            "docker image prune -f"
        )

        if not shell_result.success:
            return Result.failed_result(shell_result.stderr)

        return Result.success_result(
            data = {
                "stdout": shell_result.stdout
            }
        )

    def prune_system(self):

        shell_result = self.shell.execute(
            "docker system prune -af"
        )

        if not shell_result.success:
            return Result.failed_result(shell_result.stderr)

        return Result.success_result(
            data = {
                "stdout": shell_result.stdout
            }
        )

   
    def version(self):

        shell_result = self.shell.execute(
            "docker compose version"
        )

        if not shell_result.success:
            return Result.failed_result(shell_result.stderr)

        return Result.success_result(
            data = {
                "stdout": shell_result.stdout
            }
        )

    def docker_info(self):

        shell_result = self.shell.execute(
            "docker info"
        )

        if not shell_result.success:
            return Result.failed_result(shell_result.stderr)

        return Result.success_result(
            data = {
                "stdout": shell_result.stdout
            }
        )