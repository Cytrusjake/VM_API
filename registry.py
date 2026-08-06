class Registry:

    def __init__(self):
        self._registry = {}

    def register(self, namespace, manager):

        namespace = namespace.lower()

        if namespace in self._registry:

            raise ValueError(
                f"Manager '{namespace}' already registered."
            )

        self._registry[namespace] = manager

    def get(self, namespace):

        return self._registry.get(
            namespace.lower()
        )

    def exists(self, namespace):

        return namespace.lower() in self._registry

    def list(self):

        return sorted(self._registry.keys())

        