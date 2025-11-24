from student_repository import *

if __name__ == '__main__':
    repository = Student_repository("users.csv")
    students=repository.get_all()
    for i in students:
        print()