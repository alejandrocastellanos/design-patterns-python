from behavioral_patterns.command.controller.door_command import DoorCommand
from behavioral_patterns.command.controller.enum import Action


def test_command():
    command = DoorCommand()
    door_open = command.execute(Action.DOOR_OPEN)
    door_close = command.execute(Action.DOOR_CLOSE)
    undo = command.undo_execute()

    assert door_open == 'Door Opened'
    assert door_close == 'Door closed'
    assert undo == 'Door Opened'
