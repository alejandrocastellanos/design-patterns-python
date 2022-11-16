class BorgSingleton:
    """
        Allows state sharing for different instances.
    """
    __shared_state = {}

    """
        The __init__ method, which is called after instantiating any object
    """
    def __init__(self):
        """
            Because the class's instance's __dict__ is set equal to the __share_state dict.
            They point to the same object. (Classname.__dict__ holds all of the class attributes)
        """
        self.__dict__ = self.__shared_state
