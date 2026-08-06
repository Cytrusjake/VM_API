from managers.base import BaseManager


class LogsManager(BaseManager):

    COMMANDS = {

        "Container"         : "container",
        "ContainerFollow"   : "container_follow",
        "Journal"           : "journal",
        "Service"           : "service",
        "Search"            : "search",
        "Tail"              : "tail",
        "Follow"            : "follow",
        "Download"          : "download"

    }

    def __init__(self, context):

        super().__init__(context)

    @property
    def logs(self):

        return self.services["logs"]

   
    def container(self, params):

        return self.logs.container(

            params["Directory"],
            params["Service"],
            params.get("Lines", 100)

        )

    def container_follow(self, params):

        return self.logs.container_follow(

            params["Directory"],
            params["Service"]

        )

    
    def journal(self, params):

        return self.logs.journal(

            params.get("Lines", 100)

        )

    def service(self, params):

        return self.logs.service(

            params["Service"],
            params.get("Lines", 100)

        )

    
    def search(self, params):

        return self.logs.search(

            params["File"],
            params["Pattern"]

        )

    def tail(self, params):

        return self.logs.tail(

            params["File"],
            params.get("Lines", 100)

        )

    def follow(self, params):

        return self.logs.follow(

            params["File"]

        )

    def download(self, params):

        return self.logs.download(

            params["File"]

        )

        