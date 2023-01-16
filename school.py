"""School class which stores information about courses and students."""
import random

class School:
    def __init__(self, name):
        self.name = name
        self.__students = []
        self.__courses = []

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def add_student(self, student):
        if student not in self.__students:
            id = random.randint(1, 100)
            while any([student.get_id() == id for student in self.__students]):
                id = random.randint(1, 100)
            student.set_id(id)
            self.__students.append(student)

    def add_student_grade(self, student, course, grade: int):
        if student in self.__students and course in self.__courses:
            student.add_grade(tuple([course, grade]))
            course.add_grade(tuple([student, grade]))
    pass

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def get_students_ordered_by_average_grade(self):
        if len(self.__students) == 0:
            return []
        else:
            for i in range(len(self.__students)-1):
                if self.__students[i].get_average_grade() < self.__students[i+1].get_average_grade():
                    help = self.__students[i]
                    self.__students[i] = self.__students[i+1]
                    self.__students[i+1] = help
            return self.__students
