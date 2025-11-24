import studen_repository

if __name__ == '__main__':
    repository = studen_repository("users.csv")
    stud=repository.get_all()
    for i in stud:
        print(i)