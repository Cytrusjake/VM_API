# services/nginx.py

from result import Result


class NginxService:

    SERVICE = "nginx"

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

    def reload(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} nginx -s reload"
        )

   

    def test(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} nginx -t"
        )

    def version(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} nginx -v"
        )

    def config(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} nginx -T"
        )

    def modules(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} nginx -V"
        )

    def list_vhosts(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} ls -1 /etc/nginx/conf.d"
        )

   
    def access_log(self, directory, lines=100):

        return self.compose.logs(
            directory,
            service=self.SERVICE,
            lines=lines
        )

    def error_log(self, directory, lines=100):

        return self.compose.logs(
            directory,
            service=self.SERVICE,
            lines=lines
        )