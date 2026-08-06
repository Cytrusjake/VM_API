from managers.base import BaseManager


class NginxManager(BaseManager):

    COMMANDS = {
        "Test"          : "test",
        "Reload"        : "reload",
        "Restart"       : "restart",
        "Status"        : "status",
        "Logs"          : "logs",
        "EnableSite"    : "enable_site",
        "DisableSite"   : "disable_site",
        "InstallSSL"    : "install_ssl",
        "ForceHTTPS"    : "force_https",
        "SetHTTP2"      : "set_http2",
        "SetHTTP3"      : "set_http3",
        "SetHSTS"       : "set_hsts",
        "SetBrotli"     : "set_brotli",
        "SetGzip"       : "set_gzip",
    }

    @property
    def nginx(self):
        return self.services["nginx"]

    
    def test(self, params):
        return self.nginx.test()

    def reload(self, params):
        return self.nginx.reload()

    def restart(self, params):
        return self.nginx.restart()

    def status(self, params):
        return self.nginx.status()

   
    def logs(self, params):
        return self.nginx.logs(
            params["Directory"]
        )

    
    def enable_site(self, params):
        return self.nginx.enable_site(
            params["Site"]
        )

    def disable_site(self, params):
        return self.nginx.disable_site(
            params["Site"]
        )

    
    def install_ssl(self, params):
        return self.nginx.install_ssl(
            params["Directory"]
        )

    def force_https(self, params):
        return self.nginx.force_https(
            params["Directory"]
        )

   
    def set_http2(self, params):
        return self.nginx.set_http2(
            params["Enabled"]
        )

    def set_http3(self, params):
        return self.nginx.set_http3(
            params["Enabled"]
        )

    def set_hsts(self, params):
        return self.nginx.set_hsts(
            params["Enabled"]
        )

    def set_brotli(self, params):
        return self.nginx.set_brotli(
            params["Enabled"]
        )

    def set_gzip(self, params):
        return self.nginx.set_gzip(
            params["Enabled"]
        )

        