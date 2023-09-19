class calc:
    def add(x,y):
        return x+y
    def sub(self,x,y):
        return x - y
    def multi(self,x,y):
        return x*y
    def dived(self,x,y):
        if y != 0:
            return x/y
        else:
            print("not divide by zero")



print(calc.add(7,7))