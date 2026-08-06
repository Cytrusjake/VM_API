from result import Result


class LogsService:

    def __init__(self, compose, shell):

        self.compose = compose
        self.shell   = shell

   
    def container(
        self,
        directory,
        service,
        lines = 100
    ):

        return self.compose._run(
            directory,
            f"docker compose logs --tail {lines} {service}"
        )

    def container_follow(
        self,
        directory,
        service
    ):

        return self.compose._run(
            directory,
            f"docker compose logs -f {service}"
        )

    ####################################################################
    # System Journal
    ####################################################################

    def journal(
        self,
        lines = 100
    ):

        return self.shell.run_result(
            f"journalctl -n {lines} --no-pager"
        )

    def service(
        self,
        service,
        lines=100
    ):

        return self.shell.run_result(
            f"journalctl -u {service} -n {lines} --no-pager"
        )

   
    def search(
        self,
        logfile,
        pattern
    ):

        return self.shell.run_result(
            f'grep -n "{pattern}" {logfile}'
        )

   
    def tail(
        self,
        logfile,
        lines=100
    ):

        return self.shell.run_result(
            f"tail -n {lines} {logfile}"
        )

    
    def follow(
        self,
        logfile
    ):

        return self.shell.run_result(
            f"tail -f {logfile}"
        )

    
    def download(
        self,
        logfile
    ):

        return self.shell.run_result(
            f"cat {logfile}"
        )

        