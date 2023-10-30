class parent:
    def method(self):
        print("this is from parent method")
class child(parent):
    def method2(self):
        parent.method()
        
        
test = child()
test.method2()