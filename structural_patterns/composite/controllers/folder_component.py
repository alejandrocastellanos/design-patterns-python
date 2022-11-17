from structural_patterns.composite.controllers.component import BaseComponent


class FolderComponent(BaseComponent):

    def __init__(self, name, components):
        self._name = name
        self._components = components

    def get_size(self):
        tota_size = 0
        for component in self._components:
            tota_size += component.get_size()
        return tota_size
