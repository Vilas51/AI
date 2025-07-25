class Student:
    # name = "karan"
    def __init__(self,fullname):
        print(self)
        self.name=fullname
        print("adding new student in DB...")

s1=Student("karan")
print(s1.name)

# s2=Student()
# print(s2.name)

class Car:
    color= "blue"
    model= "mercidies"

car1=Car()
print(car1.color)
print(car1.model)

# ( __init__() ) function when object is initiated
# object attribute prcidence is higher than class attribute