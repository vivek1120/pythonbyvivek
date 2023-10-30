def check_string(str,int):
    if len(str) <= 2:
        return str * int
    else:
        first_2char = str[:2]
        return first_2char * int
    
string = input("enter a string: ")
inte = int(input("enter a number: "))

print(check_string(string,inte))