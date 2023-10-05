#variable
PI = 3.1416
GREETING = "hello world"


#functions
def multi(x,y):
    return x*y

#class
class person:
    def __init__(self,name,age,profesion,dob):
        self.name = name
        self.age = age
        self.proffesion = profesion
        self.dateofbirth = dob
    def greetings(self):
            return f"hello my name is {self.name} and my age is {self.age} and i am working in a {self.proffesion} and my dob is {self.dateofbirth}"