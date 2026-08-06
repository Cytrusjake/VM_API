# services/shell.py

import subprocess


class ShellService:

    def execute(
        self,
        command,
        cwd     = None,
        timeout = None
    ):

        result = subprocess.run(
            command,
            shell           = True,
            cwd             = cwd,
            timeout         = timeout,
            capture_output  = True,
            text            = True
        )

        return {
            "success"       : result.returncode == 0,
            "returncode"    : result.returncode,
            "stdout"        : result.stdout.strip(),
            "stderr"        : result.stderr.strip()
        }