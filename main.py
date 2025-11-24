path="users.csv"
class Stud:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.age} - {self.name}")

if __name__ == '__main__':
    stud =list()
    with open(path, "r", encoding= "utf-8") as file:
        stud1 = file.readlines()
        for i in  stud1:
            st=i.split(",")
            stud1=Stud(st[0], int(st[1]))
            stud.append(stud1)
            print(stud1.name,stud1.age)

    for i in stud: print(i)