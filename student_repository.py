import csv
class Student:

    def __init__(self, id, name,age):
        self.__id = id
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"{self.__id}: {self.__name} - {self.__age}"
    @property
    def id(self):
        return self.__id

class Student_repository:

    def __init__(self, path):
        self.__path = path

    def get_all(self):
        students = list()
        with open(self.__path, "r", encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], row[1], int(row[2]))
                students.append(student)

        return students

    def get_by_id(self, id):
        with open(self.__path, "r", encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], row[1], int(row[2]))
                if student.id == id:
                    return student
            return None


    def add(self, student):
        with open(self.__path, "r", encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], row[1], int(row[2]))
                if student.id == id:
                    return student