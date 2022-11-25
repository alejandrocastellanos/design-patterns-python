from behavioral_patterns.state.controllers.elevator import Elevator
from behavioral_patterns.state.controllers.first_floor import FirstFloor


def test_state():

    my_elevator = Elevator(FirstFloor())
    present_state = my_elevator.present_state()

    my_elevator.push_up_button()
    present_state_after_push_up_button = my_elevator.present_state()
    my_elevator.push_down_button()
    present_state_after_push_down_button = my_elevator.present_state()

    assert present_state == 'Elevator is in FirstFloor'
    assert present_state_after_push_up_button == 'Elevator is in SecondFloor'
    assert present_state_after_push_down_button == 'Elevator is in FirstFloor'
