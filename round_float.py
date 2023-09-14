def manual_round(float_number):
    if float_number >= 0:
        return int(float_number + 0.5)
    else:
        return int(float_number - 0.5)

# Example usage:
float_number = 3.7
rounded_number = manual_round(float_number)
print(rounded_number)  # Output: 4

float_number = -3.7
rounded_number = manual_round(float_number)
print(rounded_number)  # Output: -4
