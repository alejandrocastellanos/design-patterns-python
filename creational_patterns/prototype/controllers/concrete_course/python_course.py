from creational_patterns.prototype.controllers.prototype import Prototype


class PythonCourse(Prototype):

    def __init__(self):
        super().__init__()
        self._type = 'Python Basic and Algoritm'

    def course(self):
        return "Inside Python :: course() method"
