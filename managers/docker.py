from managers.base import BaseManager


class DockerManager(BaseManager):

    COMMANDS = {

        "PS"        : "ps",
        "Restart"   : "restart",
        "Stop"      : "stop",
        "Start"     : "start"

    }

    def ps(self, params):
        return self.services["docker"].ps()

    def restart(self, params):

        return self.services["docker"].restart(
            params["Container"]
        )

    def stop(self, params):

        return self.services["docker"].stop(
            params["Container"]
        )

    def start(self, params):

        return self.services["docker"].start(
            params["Container"]
        )
        