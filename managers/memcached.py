from managers.base import BaseManager


class MemcachedManager(BaseManager):

    COMMANDS = {
        "Restart"       : "restart",
        "Start"         : "start",
        "Stop"          : "stop",
        "Status"        : "status",
        "Version"       : "version",
        "Stats"         : "stats",
        "Settings"      : "settings",
        "Slabs"         : "slabs",
        "Items"         : "items",
        "Flush"         : "flush"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def memcached(self):
        return self.services["memcached"]

    
    def restart(self, params):
        return self.memcached.restart(params["Directory"])

    def start(self, params):
        return self.memcached.start(params["Directory"])

    def stop(self, params):
        return self.memcached.stop(params["Directory"])

    def status(self, params):
        return self.memcached.status(params["Directory"])

    def version(self, params):
        return self.memcached.version(params["Directory"])

    def stats(self, params):
        return self.memcached.stats(params["Directory"])

    def settings(self, params):
        return self.memcached.settings(params["Directory"])

    def slabs(self, params):
        return self.memcached.slabs(params["Directory"])

    def items(self, params):
        return self.memcached.items(params["Directory"])

    def flush(self, params):
        return self.memcached.flush(params["Directory"])

        