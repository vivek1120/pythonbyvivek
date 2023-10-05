class test:
    def __init__(self):
        self.variable = [1,2,3]
        self.Change(self.variable)
    def Change(self, var):
        var = [3,4,5]
obj=test()
print(obj.variable)