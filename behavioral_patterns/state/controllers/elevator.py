class Elevator:

    _state = None

    def __init__(self, state):
        self.set_elevator(state)

    def set_elevator(self, state):
        self._state = state
        self._state.elevator = self

    def present_state(self):
        return f'Elevator is in {type(self._state).__name__}'

    def push_down_button(self):
        self._state.push_down_button()

    def push_up_button(self):
        self._state.push_up_button()

    def push_up_and_down_buttons(self):
        return "Oops... you should press one button at a time"

    def no_button_pushed(self):
        return "Press any button. Up or Down"
