from behavioral_patterns.visitor.controllers.visitor import Visitor


class Instructor(Visitor):

    def visit(self, crop):
        return crop.teaching(self)
