def ls_string(string):
    if string[0:2] == "ls":
        return string
    else:
        return "ls" + string
print(ls_string("n"))