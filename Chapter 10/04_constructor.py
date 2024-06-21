class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Rahul = Employee("Rahul", 1300000, "JavaScript") 
# Rahul.name = "Rahul"
print(Rahul.name, Rahul.salary, Rahul.language)

# Rahul = Employee()