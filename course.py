"""Course class with name and grades."""


class Course:
    def __init__(self, name):
        self.name = name
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_grades(self) -> list:
        return self.__grades

    def get_average_grade(self) -> float:
        if len(self.__grades) == 0:
            return -1
        else:
            sum_og_grades = 0
            for grade in self.__grades:
                sum_og_grades += grade[1]
                average_grade = sum_og_grades / len(self.__grades)
            return average_grade

    def __repr__(self):
        return self.name



    pass
