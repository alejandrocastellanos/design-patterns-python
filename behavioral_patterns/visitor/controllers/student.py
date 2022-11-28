from behavioral_patterns.visitor.controllers.visitor import Visitor


class Student(Visitor):

    def visit(self, crop):
        return crop.studying(self)
