class Context:
    
    def __init__(self):

        self.logger                 = None
        self.config                 = None
        self.database               = None
        self.services               = {}
        context.services["shell"]   = ShellService()
        context.services["docker"]  = DockerService(context.services["shell"])