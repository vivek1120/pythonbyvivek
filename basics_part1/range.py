def calculate_tax(income):
    assert income >= 0, "vivek"
    
    tax_rate = 0.15
    tax_amount = income * tax_rate
    return tax_amount

# Example usage
result = calculate_tax(-5)
print(result)  # Output: 7500.0

# Uncomment the line below to see an AssertionError
# result = calculate_tax(-1000)

