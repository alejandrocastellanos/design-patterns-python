from behavioral_patterns.state.controllers.state import State


class FirstFloor(State):

    def push_down_button(self):
        return "Already in the bottom floor"

    def push_up_button(self):
        self.elevator.set_elevator(SecondFloor())
        return "Elevator moving upward one floor"


class SecondFloor(State):

    def push_down_button(self):
        self.elevator.set_elevator(FirstFloor())
        return "Elevator moving upward one floor"

    def push_up_button(self):
        return "Already in the top floor"
