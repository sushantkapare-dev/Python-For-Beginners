# . Add a static method in problem 2, to greet the user with helloclass Calculator:

class Calculator:    
    def __init__(self, num ):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")

    def squareroot(self):
        print(f"The squareroot of {self.num} is {self.num **1/2}")

    @staticmethod                   # Added static method
    def hello():
        print("Hello there")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()