def is_withinrange(inp):
    if inp <= 1000:
        if (inp - 1000) < 100:
            print("with in the range")
        else:
            print("not with in the range")
            
    elif inp <= 2000:
        if(inp - 2000) < 100:
            print("with in the range")
        else:
            print("not with in the range")
    else:
        print("not with in the range")
        

input = int(input("enter a number: "))
is_withinrange(input)