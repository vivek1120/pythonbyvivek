def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9



c = int(input("enter celsius: "))
f = int(input("enter fahranheat: "))

a = celsius_to_fahrenheit(c)
b = fahrenheit_to_celsius(f)

print(f"this is fahranheat temp:{a}")
print(f"this is celsius temp:{b}")
