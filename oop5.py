class MyClass:
    def class_attribute(self):
        print("this is instance method")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of without creating instance")

    def instance_method():
        print("This is an instance method")


# Calling class method
MyClass.class_method() 
MyClass.instance_method()

# Accessing class attribute
MyClass.class_attribute()



