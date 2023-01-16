"""Student class with student name and grades."""


class Student:
    def __init__(self, name):
        self.name = name
        self.__id = None
        self.__grades = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if self.__id == None:
            self.__id = id

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_grades(self) -> list:
        return self.__grades

    def __repr__(self):
        return self.name

    def get_average_grade(self):
        if len(self.__grades) == 0:
            return -1
        else:
            sum_og_grades = 0
            for grade in self.__grades:
                sum_og_grades += grade[1]
            average_grade = sum_og_grades / len(self.__grades)
            return average_grade

    def get_students_ordered_by_average_grade(self):
        for i in range(len(self.__students)-1):
            if not self.__students:
                return -1
            elif self.__students[i].get_average_grade() < self.__students[i+1].get_average_grade():
                help = self.__students[i]
                self.__students[i] = self.__students[i+1]
                self.__students[i+1] = help
            return self.__students

