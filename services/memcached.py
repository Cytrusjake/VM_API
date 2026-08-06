from result import Result


class MemcachedService:

    SERVICE = "memcached"

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


    def version(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} memcached -h"
        )

    def stats(self, directory):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} sh -c \'echo "stats" | nc localhost 11211\''
        )

    def settings(self, directory):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} sh -c \'echo "stats settings" | nc localhost 11211\''
        )

    def slabs(self, directory):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} sh -c \'echo "stats slabs" | nc localhost 11211\''
        )

    def items(self, directory):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} sh -c \'echo "stats items" | nc localhost 11211\''
        )

   
    def flush(self, directory):

        return self.compose._run(
            directory,
            f'docker compose exec -T {self.SERVICE} sh -c \'echo "flush_all" | nc localhost 11211\''
        )

        