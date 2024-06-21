# A class method is a method which is bound to the class and not the object of the class. 

class Emplyee:
    a = 10

    @classmethod
    def show(cls):
        """
        The @classmethod decorator is used to define a method
        that is bound to the class and not the instance of the class.
        """
        print(f"This is class attribute of a is  {cls.a}")

e = Emplyee()
e.a = 45
e.show()  # This is class method 1
