import csv
class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.age} - {self.name}")

class Student_repository:
    def __init__(self,path):
        self.__path=path

    def get_all(self):
        students = list()
        with open(self.__path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], int(row[1]))
                students.append(student)
        return students
