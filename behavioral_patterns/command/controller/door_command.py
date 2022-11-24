from behavioral_patterns.command.controller.command import Command
from behavioral_patterns.command.controller.enum import Action


class DoorCommand(Command):

    def execute(self, action: Action):
        switcher = {
            Action.DOOR_OPEN: self.door.open,
            Action.DOOR_CLOSE: self.door.close
        }
        self.last_action = action
        function = switcher.get(action)
        return function()

    def undo_execute(self):
        switcher = {
            Action.DOOR_OPEN: self.door.close,
            Action.DOOR_CLOSE: self.door.open
        }
        function = switcher.get(self.last_action)
        return function()
