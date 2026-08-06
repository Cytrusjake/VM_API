from result import Result


class ResourcesService:

    def __init__(self, shell):
        self.shell = shell

    def cpu(self):

        return self.shell.run_result(
            "top -bn1 | grep '%Cpu'"
        )

    
    def memory(self):

        return self.shell.run_result(
            "free -h"
        )


    def disk(self):

        return self.shell.run_result(
            "df -h"
        )

   
    def load(self):

        return self.shell.run_result(
            "uptime"
        )

    
    def uptime(self):

        return self.shell.run_result(
            "uptime -p"
        )

    
    def network(self):

        return self.shell.run_result(
            "ip addr"
        )

    
    def processes(self):

        return self.shell.run_result(
            "ps aux --sort=-%mem | head -25"
        )

    
    def users(self):

        return self.shell.run_result(
            "who"
        )

    
    def kernel(self):

        return self.shell.run_result(
            "uname -a"
        )

    
    def hostname(self):

        return self.shell.run_result(
            "hostname"
        )

        