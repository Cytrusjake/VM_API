from managers.base import BaseManager


class PHPManager(BaseManager):

    COMMANDS = {
        "Version"               : "version",
        "Info"                  : "info",
        "Modules"               : "modules",
        "Configuration"         : "configuration",
        "RestartFPM"            : "restart_fpm",
        "ReloadFPM"             : "reload_fpm",
        "OpcacheReset"          : "opcache_reset",
        "SetMemoryLimit"        : "set_memory_limit",
        "SetUploadMaxFilesize"  : "set_upload_max_filesize",
        "SetPostMaxSize"        : "set_post_max_size",
        "SetMaxExecutionTime"   : "set_max_execution_time",
        "SetMaxInputTime"       : "set_max_input_time",
        "SetMaxInputVars"       : "set_max_input_vars",
        "SetDisplayErrors"      : "set_display_errors",
        "SetErrorReporting"     : "set_error_reporting",
        "SetLogErrors"          : "set_log_errors",
        "SetDefaultCharset"     : "set_default_charset",
        "SetTimezone"           : "set_timezone"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def php(self):
        return self.services["php"]

   
    def version(self, params):
        return self.php.version(params["Directory"])

    def info(self, params):
        return self.php.info(params["Directory"])

    def modules(self, params):
        return self.php.modules(params["Directory"])

    def configuration(self, params):
        return self.php.configuration(params["Directory"])

    def restart_fpm(self, params):
        return self.php.restart_fpm(params["Directory"])

    def reload_fpm(self, params):
        return self.php.reload_fpm(params["Directory"])

    def opcache_reset(self, params):
        return self.php.opcache_reset(params["Directory"])

    def set_memory_limit(self, params):
        return self.php.set_memory_limit(
            params["Directory"],
            params["Value"]
        )

    def set_upload_max_filesize(self, params):
        return self.php.set_upload_max_filesize(
            params["Directory"],
            params["Value"]
        )

    def set_post_max_size(self, params):
        return self.php.set_post_max_size(
            params["Directory"],
            params["Value"]
        )

    def set_max_execution_time(self, params):
        return self.php.set_max_execution_time(
            params["Directory"],
            params["Value"]
        )

    def set_max_input_time(self, params):
        return self.php.set_max_input_time(
            params["Directory"],
            params["Value"]
        )

    def set_max_input_vars(self, params):
        return self.php.set_max_input_vars(
            params["Directory"],
            params["Value"]
        )

    def set_display_errors(self, params):
        return self.php.set_display_errors(
            params["Directory"],
            params["Value"]
        )

    def set_error_reporting(self, params):
        return self.php.set_error_reporting(
            params["Directory"],
            params["Value"]
        )

    def set_log_errors(self, params):
        return self.php.set_log_errors(
            params["Directory"],
            params["Value"]
        )

    def set_default_charset(self, params):
        return self.php.set_default_charset(
            params["Directory"],
            params["Value"]
        )

    def set_timezone(self, params):
        return self.php.set_timezone(
            params["Directory"],
            params["Value"]
        )