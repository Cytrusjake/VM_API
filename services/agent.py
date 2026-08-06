from result import Result


class AgentService:

    def __init__(self, shell):

        self.shell = shell

    
    def git_pull(self, directory):

        return self.shell.run_result(
            f'cd "{directory}" && git pull'
        )

    
    def version(self, directory):

        return self.shell.run_result(
            f'cd "{directory}" && git rev-parse --short HEAD'
        )

    def branch(self, directory):

        return self.shell.run_result(
            f'cd "{directory}" && git branch --show-current'
        )

    
    def restart(self, service):

        return self.shell.run_result(
            f"systemctl restart {service}"
        )

    def status(self, service):

        return self.shell.run_result(
            f"systemctl status {service} --no-pager"
        )

    
    def ping(self):

        return Result.success_result(
            message="Pong"
        )