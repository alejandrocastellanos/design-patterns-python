from structural_patterns.proxy.controller.door import Door


class SecuredDoor:

    def __init__(self):
        self.door = Door()

    def open_door(self):
        return self.door.open_door()
