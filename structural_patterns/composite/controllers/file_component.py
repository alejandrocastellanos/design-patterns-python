from structural_patterns.composite.controllers.component import BaseComponent


class FileComponent(BaseComponent):

    def __init__(self, name, size):
        self._name = name
        self._size = size

    def get_size(self):
        return self._size
