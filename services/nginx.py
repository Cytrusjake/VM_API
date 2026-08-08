from pathlib import Path
from result import Result


class NginxService:

    SERVICE         = "nginx"
    VHOST_DIRECTORY = Path("/etc/tenant-nginx/conf.d")

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
            f"ls -1 {self.VHOST_DIRECTORY}"
        )



    def add_vhost(self, directory, domain, contents):

        self.VHOST_DIRECTORY.mkdir(parents = True, exist_ok = True)

        filename = self.VHOST_DIRECTORY / f"{domain}.conf"

        filename.write_text(contents, encoding = "utf-8")

        result = self.test(directory)

        if not result.success:
            filename.unlink(missing_ok=True)
            return result

        return self.reload(directory)

    def remove_vhost(self, directory, domain):

        filename = self.VHOST_DIRECTORY / f"{domain}.conf"

        if filename.exists():
            filename.unlink()

        result = self.test(directory)

        if not result.success:
            return result

        return self.reload(directory)

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