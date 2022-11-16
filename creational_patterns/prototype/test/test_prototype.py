from creational_patterns.prototype.controllers.course_cache.course_cache import CoursesCache


def test_prototype():
    CoursesCache.load()
    python = CoursesCache().get_course("1")
    java = CoursesCache.get_course("2")

    python_type = python.get_type()
    java_type = java.get_type()

    assert python_type == 'Python Basic and Algoritm'
    assert java_type == 'Java Basics and Spring Boot'
