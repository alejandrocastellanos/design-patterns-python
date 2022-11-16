from creational_patterns.prototype.controllers.prototype import Prototype


class JavaCourse(Prototype):

    def __init__(self):
        super().__init__()
        self._type = 'Java Basics and Spring Boot'

    def course(self):
        return "Inside Java :: course() method"
