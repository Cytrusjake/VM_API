from managers.base import BaseManager


class VarnishManager(BaseManager):

    COMMANDS = {
        "Restart"       : "restart",
        "Start"         : "start",
        "Stop"          : "stop",
        "Status"        : "status",
        "PurgeAll"      : "purge_all",
        "PurgeURL"      : "purge_url",
        "Ban"           : "ban",
        "Stats"         : "stats",
        "HitRate"       : "hit_rate",
        "Backend"       : "backend",
        "Config"        : "config",
        "Version"       : "version"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def varnish(self):
        return self.services["varnish"]

    def restart(self, params):
        return self.varnish.restart(params["Directory"])

    def start(self, params):
        return self.varnish.start(params["Directory"])

    def stop(self, params):
        return self.varnish.stop(params["Directory"])

    def status(self, params):
        return self.varnish.status(params["Directory"])


    def purge_all(self, params):
        return self.varnish.purge_all(params["Directory"])

    def purge_url(self, params):
        return self.varnish.purge_url(
            params["Directory"],
            params["URL"]
        )

    def ban(self, params):
        return self.varnish.ban(
            params["Directory"],
            params["Expression"]
        )

    
    def stats(self, params):
        return self.varnish.stats(params["Directory"])

    def hit_rate(self, params):
        return self.varnish.hit_rate(params["Directory"])

    def backend(self, params):
        return self.varnish.backend(params["Directory"])

    def config(self, params):
        return self.varnish.config(params["Directory"])

    def version(self, params):
        return self.varnish.version(params["Directory"])

        