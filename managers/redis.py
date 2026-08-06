from managers.base import BaseManager


class RedisManager(BaseManager):

    COMMANDS = {
        "Restart"           : "restart",
        "Start"             : "start",
        "Stop"              : "stop",
        "Status"            : "status",
        "Version"           : "version",
        "Info"              : "info",
        "Memory"            : "memory",
        "Clients"           : "clients",
        "SlowLog"           : "slow_log",
        "FlushAll"          : "flush_all",
        "FlushDB"           : "flush_db",
        "Stats"             : "stats",
        "Persistence"       : "persistence",
        "Replication"       : "replication",
        "KeyCount"          : "key_count",
        "Keys"              : "keys",

        "Ping": "ping",
        "Save": "save",
        "BackgroundSave": "bgsave"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def redis(self):
        return self.services["redis"]

    def restart(self, params):
        return self.redis.restart(params["Directory"])

    def start(self, params):
        return self.redis.start(params["Directory"])

    def stop(self, params):
        return self.redis.stop(params["Directory"])

    def status(self, params):
        return self.redis.status(params["Directory"])

    def version(self, params):
        return self.redis.version(params["Directory"])

    def info(self, params):
        return self.redis.info(params["Directory"])

    def memory(self, params):
        return self.redis.memory(params["Directory"])

    def clients(self, params):
        return self.redis.clients(params["Directory"])

    def slow_log(self, params):
        return self.redis.slow_log(params["Directory"])

   
    def flush_all(self, params):
        return self.redis.flush_all(params["Directory"])

    def flush_db(self, params):
        return self.redis.flush_db(params["Directory"])

    def stats(self, params):
        return self.redis.stats(params["Directory"])

    def persistence(self, params):
        return self.redis.persistence(params["Directory"])

    def replication(self, params):
        return self.redis.replication(params["Directory"])

   
    def key_count(self, params):
        return self.redis.key_count(params["Directory"])

    def keys(self, params):
        return self.redis.keys(
            params["Directory"],
            params.get("Pattern", "*")
        )


    def ping(self, params):
        return self.redis.ping(params["Directory"])

    def save(self, params):
        return self.redis.save(params["Directory"])

    def bgsave(self, params):
        return self.redis.bgsave(params["Directory"])

        