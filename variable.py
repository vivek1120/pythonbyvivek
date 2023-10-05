my_variable = 65 #direct assignement

var1, var2, var3 = "var1", "var2", 43 # multiple assignments
print(var1)

def ass_var():
    return "value1","value2"

varfun1, varfun2 = ass_var()

print(varfun1)
print(type(varfun1)) #assigning by function return


x = 10
y = 10 
z = 10

print(x, y, z)
print(id(x))
print(id(y))
print(id(z))