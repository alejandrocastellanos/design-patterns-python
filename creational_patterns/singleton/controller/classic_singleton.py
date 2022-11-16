class DBClassicSingleton:

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(self):
        if self._initialized is True:
            return
        # Connection with DB
        DBClassicSingleton._initialized = True
