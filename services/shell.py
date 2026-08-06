import subprocess

from result import Result


class ShellService:

    ####################################################################
    # Execute
    ####################################################################

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

        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }

    ####################################################################
    # Execute and return Result
    ####################################################################

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

        if response["success"]:

            return Result.success_result(
                data={
                    "stdout": response["stdout"]
                }
            )

        return Result.failed_result(
            error=response["stderr"]
        )