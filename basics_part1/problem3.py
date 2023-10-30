def sum_of_num(x,y,z):
    if x == y == z:
        result = x + y + z
        return result * 3
    else:
        return x + y + z

result = sum_of_num(1, 5, 5)
print(result)