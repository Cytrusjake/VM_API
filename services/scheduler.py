from result import Result


class SchedulerService:

    SERVICE = "cron"

    def __init__(self, compose):

        self.compose = compose

    
    def restart(self, directory):

        return self.compose._run(
            directory,
            f"docker compose restart {self.SERVICE}"
        )

    def start(self, directory):

        return self.compose._run(
            directory,
            f"docker compose start {self.SERVICE}"
        )

    def stop(self, directory):

        return self.compose._run(
            directory,
            f"docker compose stop {self.SERVICE}"
        )

    def status(self, directory):

        return self.compose._run(
            directory,
            f"docker compose ps {self.SERVICE}"
        )

   
    def list(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} crontab -l"
        )

    def install(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} "
            f"crontab /etc/tenant-cron/crontab"
        )

    def remove_all(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} crontab -r"
        )

    def add(self, directory, expression):

        command = (
            f'docker compose exec -T {self.SERVICE} sh -c '
            f'"(crontab -l 2>/dev/null; echo \'{expression}\') | crontab -"'
        )

        return self.compose._run(
            directory,
            command
        )

    def remove(self, directory, expression):

        command = (
            f'docker compose exec -T {self.SERVICE} sh -c '
            f'"crontab -l | grep -F -v \'{expression}\' | crontab -"'
        )

        return self.compose._run(
            directory,
            command
        )

    def enable(self, directory, expression):

        command = (
            f'docker compose exec -T {self.SERVICE} sh -c '
            f'"crontab -l | '
            f'sed \'s/^# *\\({expression}\\)/\\1/\' | '
            f'crontab -"'
        )

        return self.compose._run(
            directory,
            command
        )

    def disable(self, directory, expression):

        command = (
            f'docker compose exec -T {self.SERVICE} sh -c '
            f'"crontab -l | '
            f'sed \'s/^\\({expression}\\)/# \\1/\' | '
            f'crontab -"'
        )

        return self.compose._run(
            directory,
            command
        )

   
    def run(self, directory, command):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} {command}"
        )