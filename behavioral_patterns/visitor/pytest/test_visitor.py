from behavioral_patterns.visitor.controllers.concrete_class import SDE, STL, DSA
from behavioral_patterns.visitor.controllers.instructor import Instructor
from behavioral_patterns.visitor.controllers.student import Student


def test_visitor():

    sde = SDE()

    instructor = Instructor()
    student = Student()

    sde_accept_instructor = sde.accept(instructor)
    sde_accept_student = sde.accept(student)

    assert sde_accept_instructor == 'SDE Taught by Instructor'
    assert sde_accept_student == 'SDE Studied by Student'
