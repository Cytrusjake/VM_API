from managers.base import BaseManager


class NginxManager(BaseManager):

    COMMANDS = {
        "Status"        : "status",
        "Start"         : "start",
        "Stop"          : "stop",
        "Restart"       : "restart",
        "Reload"        : "reload",
        "Test"          : "test",
        "Version"       : "version",
        "Config"        : "config",
        "Modules"       : "modules",
        "ListVHosts"    : "list_vhosts",
        "AddVHost"      : "add_vhost",
        "RemoveVHost"   : "remove_vhost",
        "AccessLog"     : "access_log",
        "ErrorLog"      : "error_log"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def nginx(self):
        return self.services["nginx"]

   

    def status(self, params):
        return self.nginx.status(
            params["Directory"]
        )

    def start(self, params):
        return self.nginx.start(
            params["Directory"]
        )

    def stop(self, params):
        return self.nginx.stop(
            params["Directory"]
        )

    def restart(self, params):
        return self.nginx.restart(
            params["Directory"]
        )

    def reload(self, params):
        return self.nginx.reload(
            params["Directory"]
        )

   
    def test(self, params):
        return self.nginx.test(
            params["Directory"]
        )

    def version(self, params):
        return self.nginx.version(
            params["Directory"]
        )

    def config(self, params):
        return self.nginx.config(
            params["Directory"]
        )

    def modules(self, params):
        return self.nginx.modules(
            params["Directory"]
        )

    def list_vhosts(self, params):
        return self.nginx.list_vhosts(
            params["Directory"]
        )

    
    def add_vhost(self, params):
        return self.nginx.add_vhost(
            params["Directory"],
            params["Domain"],
            params["Contents"]
        )

    def remove_vhost(self, params):
        return self.nginx.remove_vhost(
            params["Directory"],
            params["Domain"]
        )

    

    def access_log(self, params):
        return self.nginx.access_log(
            params["Directory"]
        )

    def error_log(self, params):
        return self.nginx.error_log(
            params["Directory"]
        )