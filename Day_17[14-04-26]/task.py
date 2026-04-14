# Dequeue  => list -like container appends from both end and deletes from both end

# from collections import deque

# x = deque([1, 2, 34, 556])
# print(x, type(x))

# append()=> add to the end  appendLeft() => add in the start
#
# x.append(67)
# x.appendleft(56)
# print(x)

# pop()=> removes from the last  popleft() => removes from the start
# x.pop()
# print(x)
# x.popleft()
# print(x)

# extend(list) => adds the list element individually to the existing list at the end
# extendleft(list) => adds the list element individually to the existing list at the start
# x.extend([90, 89, 88, 87])
# print(x)
# x.extendleft([80, 89, 78, 77])
# print(x)
# ....................................................................................
from collections import defaultdict

# x = defaultdict(int)
# print(x["a"], x)
# x["a"] += 1
# print(x["a"], x)
# ........................................................................
records = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C"),
    ("Eva", "B"),
    ("Frank", "A"),
]
# {"A": ["Alice", "Charlie", "Frank"], "B": ["Bob", "Eva"], "C": ["David"]}
# .....................................................................................
# NAMED TUPLE

# from collections import namedtuple

# detail = []
# Student = namedtuple("Student", ["name", "marks", "roll"])
# # x = namedtuple("Student", ["name", "marks", "roll"])
# print(Student)
# y = Student("Sam", 567, 9)
# detail.append(y)
# print(y, detail)

# Create an Employee namedtuple and have salary, age, name, department and empID.Compute the average age.

# sarika@learntek.com
# sarika.gmail.com

# ......................................................................................................
# OOPS => Object Oriented Programming Language (Poops)

# CLASS => Blueprint
# OBJECTS => instance of the class


# class Employee:
#     language = "Python"  # class attribute
#     salary = 25000  # class attribute
#     name = "JOE"

#     def getInfo(self):
#         print(
#             f"The details of the employee: name=>{self.name} language=>{self.language} salary=>{self.salary}"
#         )

#     @staticmethod
#     def greet():
#         print("Good Evening!....")


# x = Employee()  # object / instance
# y = Employee()
# y.name = "SAM"  # instance attributes
# x.name = "DANNY"
# # print(x.language)
# # print(y.language)
# # print(y.name, x.name)
# # Instance Attributes take preference over class attributes
# y.getInfo()
# x.getInfo()
# y.greet()


# class Car:
#     # construtor
#     def __init__(self, brand, model):  # dunder method
#         self.brand = brand
#         self.model = model


# x = Car("Toyota", "Corolla")
# print(x.model, x.brand)
# .....................................................................
# INHERITANCE => creating a new class from the existing class


# class Employee:
#     name = "SAM"
#     salary = 250000
#     language = "Python"

#     def show(self):
#         print(f"The Name is : {self.name} and salary is {self.salary}")


# class Programmer(Employee):
#     company = "DTC InfoTech"
#     language = "Java"  # overwrite the parent class attribute

#     def showLanguage(self):
#         print(f"The name is {self.name}. He/She is good at {self.language}")


# a = Employee()
# b = Programmer()
# a.show()
# b.show()
# b.showLanguage()

# Single Inheritance
# Multiple Inheritance
# P1 P2
# child

# class P1:

# class P2:

# class Child(P1,P2):

# Multilevel Inheritance

# P
# C1
# C2

# class P :
# class C1(P):

# class C2(C1):


class Employee:
    def __init__(self):
        print("I am a constructor of Employee")

    a = 1


class Programmer(Employee):
    def __init__(self):
        print("I am a constructor of Programmer")

    b = 90


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("I am a constructor of Manager")

    c = 101


emp = Employee()
# pro = Programmer()
man = Manager()
# print(emp.a, man.a, pro.a, man.c)
