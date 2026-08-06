from managers.base import BaseManager


class ResourcesManager(BaseManager):

    COMMANDS = {
        "CPU"       : "cpu",
        "Memory"    : "memory",
        "Disk"      : "disk",
        "Load"      : "load",
        "Uptime"    : "uptime",
        "Network"   : "network",
        "Processes" : "processes",
        "Users"     : "users",
        "Kernel"    : "kernel",
        "Hostname"  : "hostname"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def resources(self):
        return self.services["resources"]

    def cpu(self, params):
        return self.resources.cpu()

    def memory(self, params):
        return self.resources.memory()

    def disk(self, params):
        return self.resources.disk()

    def load(self, params):
        return self.resources.load()

    def uptime(self, params):
        return self.resources.uptime()

    def network(self, params):
        return self.resources.network()

    def processes(self, params):
        return self.resources.processes()

    def users(self, params):
        return self.resources.users()

    def kernel(self, params):
        return self.resources.kernel()

    def hostname(self, params):
        return self.resources.hostname()

        