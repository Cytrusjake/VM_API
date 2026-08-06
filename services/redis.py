from result import Result


class RedisService:

    def __init__(self, compose):
        self.compose = compose

    ####################################################################
    # Service Control
    ####################################################################

    def restart(self, directory):

        return self.compose._run(
            directory,
            "docker compose restart redis"
        )

    def start(self, directory):

        return self.compose._run(
            directory,
            "docker compose start redis"
        )

    def stop(self, directory):

        return self.compose._run(
            directory,
            "docker compose stop redis"
        )

    def status(self, directory):

        return self.compose._run(
            directory,
            "docker compose ps redis"
        )

   
    def version(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-server --version"
        )

    def info(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli INFO"
        )

    def memory(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli INFO MEMORY"
        )

    def clients(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli CLIENT LIST"
        )

    def slow_log(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli SLOWLOG GET"
        )

   
    def flush_all(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli FLUSHALL"
        )

    def flush_db(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli FLUSHDB"
        )

    
    def stats(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli INFO STATS"
        )

    def persistence(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli INFO PERSISTENCE"
        )

    def replication(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli INFO REPLICATION"
        )

   
    def key_count(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli DBSIZE"
        )

    def keys(self, directory, pattern="*"):

        return self.compose._run(
            directory,
            f'docker compose exec -T redis redis-cli KEYS "{pattern}"'
        )

    
    def ping(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli PING"
        )

    def save(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli SAVE"
        )

    def bgsave(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T redis redis-cli BGSAVE"
        )

        