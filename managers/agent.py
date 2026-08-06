from managers.base import BaseManager


class AgentManager(BaseManager):

    COMMANDS = {
        "GitPull"   : "git_pull",
        "Version"   : "version",
        "Branch"    : "branch",
        "Restart"   : "restart",
        "Status"    : "status",
        "Ping"      : "ping"
    }

    @property
    def agent(self):
        return self.services["agent"]

   
    def git_pull(self, params):

        return self.agent.git_pull(
            params["Directory"]
        )

    def version(self, params):

        return self.agent.version(
            params["Directory"]
        )

    def branch(self, params):

        return self.agent.branch(
            params["Directory"]
        )

    
    def restart(self, params):

        return self.agent.restart(
            params["Service"]
        )

    def status(self, params):

        return self.agent.status(
            params["Service"]
        )

   
    def ping(self, params):

        return self.agent.ping()
        