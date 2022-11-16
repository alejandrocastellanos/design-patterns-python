from creational_patterns.prototype.controllers.concrete_course.java_course import JavaCourse
from creational_patterns.prototype.controllers.concrete_course.python_course import PythonCourse


class CoursesCache:

    cache = {}

    @staticmethod
    def get_course(sid):
        course = CoursesCache.cache.get(sid, None)
        return course.clone()

    @staticmethod
    def load():
        python = PythonCourse()
        python.set_id("1")
        CoursesCache.cache[python.get_id()] = python

        java = JavaCourse()
        java.set_id("2")
        CoursesCache.cache[java.get_id()] = java

