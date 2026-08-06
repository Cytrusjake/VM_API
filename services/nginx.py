# services/nginx.py

from result import Result


class NginxService:

    def __init__(self, compose):
        self.compose = compose

    def restart(self, directory):

        return self.compose._run(
            directory,
            "docker compose restart nginx"
        )

    def start(self, directory):

        return self.compose._run(
            directory,
            "docker compose start nginx"
        )

    def stop(self, directory):

        return self.compose._run(
            directory,
            "docker compose stop nginx"
        )

    def reload(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T nginx nginx -s reload"
        )

   
    def test(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T nginx nginx -t"
        )

    def version(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T nginx nginx -v"
        )

    def list_vhosts(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T nginx ls -1 /etc/nginx/conf.d"
        )

    
    def access_log(self, directory, lines = 100):

        return self.compose.logs(
            directory,
            service = "nginx",
            lines   = lines
        )

    def error_log(self, directory, lines=100):

        return self.compose.logs(
            directory,
            service = "nginx",
            lines   = lines
        )

    
    def config(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T nginx nginx -T"
        )

    
    def modules(self, directory):

        return self.compose._run(
            directory,
            "docker compose exec -T nginx nginx -V"
        )

        