from result import Result


class VarnishService:

    SERVICE = "varnish"

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

    
    def purge_all(self, directory):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} varnishadm "ban req.url ~ ."'
        )

    def purge_url(self, directory, url):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} varnishadm "ban req.url == {url}"'
        )

    def ban(self, directory, expression):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} varnishadm "ban {expression}"'
        )

    
    def stats(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} varnishstat"
        )

    def hit_rate(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} varnishstat -1"
        )

    def backend(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} varnishadm backend.list"
        )

    
    def config(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} varnishadm param.show"
        )

    def version(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} varnishd -V"
        )

        