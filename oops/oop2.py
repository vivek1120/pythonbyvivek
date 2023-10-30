class Dog:
    def __init__(self, name, breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    @classmethod 
    def get_info(self):
        return f"name of the dog is {self.name} and the breed is {self.breed} and also age is {self.age}"
    
    def bark(self):
        print("Woof!")
