def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = 8
b = 4

result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")
