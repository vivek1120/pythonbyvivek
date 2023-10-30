def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(57))
print(difference(14))


def calculate_difference(number):
    absolute_difference = abs(number - 17)
    
    if number > 17:
        return 2 * absolute_difference
    else:
        return absolute_difference
print(calculate_difference(20))  # This will return 6
print(calculate_difference(15))  # This will return 2
