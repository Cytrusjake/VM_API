from managers.base import BaseManager


class SchedulerManager(BaseManager):

    COMMANDS = {

        "Restart"  : "restart",
        "Start"    : "start",
        "Stop"     : "stop",
        "Status"   : "status",
        "List"     : "list",
        "Install"  : "install",
        "RemoveAll": "remove_all",
        "Add"      : "add",
        "Remove"   : "remove",
        "Enable"   : "enable",
        "Disable"  : "disable",
        "Run"      : "run"

    }

    def __init__(self, context):

        super().__init__(context)

    @property
    def scheduler(self):

        return self.services["scheduler"]

    
    def restart(self, params):

        return self.scheduler.restart(
            params["Directory"]
        )

    def start(self, params):

        return self.scheduler.start(
            params["Directory"]
        )

    def stop(self, params):

        return self.scheduler.stop(
            params["Directory"]
        )

    def status(self, params):

        return self.scheduler.status(
            params["Directory"]
        )
    

    def list(self, params):

        return self.scheduler.list(
            params["Directory"]
        )

    def install(self, params):

        return self.scheduler.install(
            params["Directory"]
        )

    def remove_all(self, params):

        return self.scheduler.remove_all(
            params["Directory"]
        )

    def add(self, params):

        return self.scheduler.add(
            params["Directory"],
            params["Expression"]
        )

    def remove(self, params):

        return self.scheduler.remove(
            params["Directory"],
            params["Expression"]
        )

    def enable(self, params):

        return self.scheduler.enable(
            params["Directory"],
            params["Expression"]
        )

    def disable(self, params):

        return self.scheduler.disable(
            params["Directory"],
            params["Expression"]
        )

   
    def run(self, params):

        return self.scheduler.run(
            params["Directory"],
            params["Command"]
        )