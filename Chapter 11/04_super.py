# Super Method

class Employee:
    def __init__(self):
        print("This is Employee Constructor")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("This is Programmers Constructor")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()          # Using Super method
        print("This is Managers Constructor")
    c = 3

# o = Employee()
# print(o.a)    
# # print(o.b)      

# o = Programmer()
# print(o.a , o.b)      

o = Manager()
print(o.a , o.b, o.c) 
