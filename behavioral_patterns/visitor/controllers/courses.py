class Courses:

    def accept(self, visitor):
        return visitor.visit(self)

    def teaching(self, visitor):
        return f'{self} Taught by {visitor}'

    def studying(self, visitor):
        return f'{self} Studied by {visitor}'

    def __str__(self):
        return self.__class__.__name__
