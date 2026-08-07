import subprocess

from result import Result


class ShellService:

   
    def execute(
        self,
        command,
        cwd=None,
        timeout=None
    ):

        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            timeout=timeout,
            capture_output=True,
            text=True
        )

        class Response:
            pass

        response = Response()

        response.success = (result.returncode == 0)
        response.returncode = result.returncode
        response.stdout = result.stdout.strip()
        response.stderr = result.stderr.strip()

        return response

   
    def run_result(
        self,
        command,
        cwd=None,
        timeout=None
    ):

        response = self.execute(
            command,
            cwd=cwd,
            timeout=timeout
        )

        if response.success:

            return Result.success_result(
                data={
                    "stdout": response.stdout,
                    "stderr": response.stderr
                }
            )

        return Result.failed_result(
            error=response.stderr
        )