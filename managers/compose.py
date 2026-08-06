from managers.base import BaseManager


class ComposeManager(BaseManager):

    COMMANDS = {
        "Deploy"        : "deploy",
        "Pull"          : "pull",
        "Up"            : "up",
        "Down"          : "down",
        "Restart"       : "restart",
        "Stop"          : "stop",
        "Start"         : "start",
        "Build"         : "build",
        "Status"        : "status",
        "Logs"          : "logs",
        "Images"        : "images",
        "Config"        : "config",
        "Validate"      : "validate",
        "Update"        : "update",
        "Rebuild"       : "rebuild",
        "Version"       : "version",
        "DockerInfo"    : "docker_info",
        "PruneImages"   : "prune_images",
        "PruneSystem"   : "prune_system"
    }

    @property
    def compose(self):
        return self.services["compose"]

    def deploy(self, params):
        return self.compose.deploy(params["Directory"])

    def pull(self, params):
        return self.compose.pull(params["Directory"])

    def up(self, params):
        return self.compose.up(
            params["Directory"],
            params.get("Detach", True)
        )

    def down(self, params):
        return self.compose.down(params["Directory"])

    def restart(self, params):
        return self.compose.restart(params["Directory"])

    def stop(self, params):
        return self.compose.stop(params["Directory"])

    def start(self, params):
        return self.compose.start(params["Directory"])

    def build(self, params):
        return self.compose.build(params["Directory"])

    def status(self, params):
        return self.compose.ps(params["Directory"])

    def logs(self, params):
        return self.compose.logs(
            params["Directory"],
            params.get("Service"),
            params.get("Lines", 100)
        )

    def images(self, params):
        return self.compose.images(params["Directory"])

    def config(self, params):
        return self.compose.config(params["Directory"])

    def validate(self, params):
        return self.compose.validate(params["Directory"])

    def update(self, params):
        return self.compose.update(params["Directory"])

    def rebuild(self, params):
        return self.compose.rebuild(params["Directory"])

    def version(self, params):
        return self.compose.version()

    def docker_info(self, params):
        return self.compose.docker_info()

    def prune_images(self, params):
        return self.compose.prune_images()

    def prune_system(self, params):
        return self.compose.prune_system()
        