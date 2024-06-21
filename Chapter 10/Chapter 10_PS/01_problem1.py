# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    Company: "Microsoft"
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

p = Programmer("Blaise", "Developer", 100000)
print(p.name , p.role, p.salary) 

r = Programmer("Raju", "Manager", 200000)
print(r.name, r.role, r.salary)
    