class Employee:
    Company = "Apple"
    def show(self):
        print(f"The  name of the Employee is {self.name} and the salary  is {self.salary}")

# class Programmer:
#     company = "Microsoft"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    Company = "Microsoft"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.Company , b.Company)
