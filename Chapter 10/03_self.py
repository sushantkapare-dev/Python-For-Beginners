class employee:
    language = "PY"     # This is class attribute
    salary = 5000

    def getInfo(self):
        print(f"The languahe  is {self.language} , The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

    
harry = employee()
harry.getInfo()
harry.greet()