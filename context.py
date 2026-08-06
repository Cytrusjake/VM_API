class Context:

    def __init__(self, logger, config):

        self.logger     = logger
        self.config     = config
        self.services   = {}