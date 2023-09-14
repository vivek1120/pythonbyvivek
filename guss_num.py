import random

x =  random.randint(1,9)

while True:
    user = int(input("enter a number bet 1 to 9: "))
    if x == user:
        print("your gussed the number")
        break
    print("try again")
    continue







