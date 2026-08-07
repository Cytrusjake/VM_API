# services/php.py

class PHPService:

    def __init__(self, compose):
        self.compose = compose

   
    def version(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T php php -v"
        )

    def info(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T php php -i"
        )

    def modules(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T php php -m"
        )

    def configuration(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T php php --ini"
        )

   
    def restart_fpm(self, directory):

        return self.compose._run(
            directory,
            "docker compose restart php"
        )

    def reload_fpm(self, directory):

        return self.compose._run(
            directory,
            'docker compose exec -T php sh -c "kill -USR2 1"'
        )

   
    def opcache_reset(self, directory):

        return self.compose._run(
            directory,
            'docker compose exec -T php php -r "if(function_exists(\'opcache_reset\')) opcache_reset();"'
        )

   
    def set_memory_limit(self, directory, value):

        return self._set_ini(
            directory,
            "memory_limit",
            value
        )

    def set_upload_max_filesize(self, directory, value):

        return self._set_ini(
            directory,
            "upload_max_filesize",
            value
        )

    def set_post_max_size(self, directory, value):

        return self._set_ini(
            directory,
            "post_max_size",
            value
        )

    def set_max_execution_time(self, directory, value):

        return self._set_ini(
            directory,
            "max_execution_time",
            value
        )

    def set_max_input_time(self, directory, value):

        return self._set_ini(
            directory,
            "max_input_time",
            value
        )

    def set_max_input_vars(self, directory, value):

        return self._set_ini(
            directory,
            "max_input_vars",
            value
        )

    def set_display_errors(self, directory, value):

        value = "On" if value else "Off"

        return self._set_ini(
            directory,
            "display_errors",
            value
        )

    def set_error_reporting(self, directory, value):

        return self._set_ini(
            directory,
            "error_reporting",
            value
        )

    def set_log_errors(self, directory, value):

        value = "On" if value else "Off"

        return self._set_ini(
            directory,
            "log_errors",
            value
        )

    def set_default_charset(self, directory, value):

        return self._set_ini(
            directory,
            "default_charset",
            value
        )

    def set_timezone(self, directory, value):

        return self._set_ini(
            directory,
            "date.timezone",
            value
        )

   
    def _set_ini(self, directory, key, value):

        command = (
            "docker compose exec -T php "
            f"sed -i 's|^;*{key} *=.*|{key} = {value}|' "
            "/usr/local/etc/php/php.ini"
        )

        result = self.compose._run(
            directory,
            command
        )

        if not result.success:
            return result

        return self.reload_fpm(directory)


    def get_setting(self, directory, key):

        return self.compose._run(
            directory,
            f'docker compose exec -T php php -i | grep "^{key}"'
        )


    def phpinfo_html(self, directory):

        return self.compose._run(
            directory,
            'docker compose exec -T php php -r "phpinfo();"'
        )


    def extensions(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T php php -m"
        )


    def installed_packages(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T php pecl list"
        )