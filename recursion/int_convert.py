def to_string(n, base):
    """
    Recursively converts an integer to its string representation in the specified base.

    Args:
        n (int): The integer to be converted.
        base (int): The target base for the conversion.

    Returns:
        str: The string representation of 'n' in the specified base.
    """
    conver_tString = "0123456789ABCDEF"

    if n < base:
        return conver_tString[n]
    else:
        return to_string(n // base, base) + conver_tString[n % base]

# Example usage:
result = to_string(2835, 16)
print(result)  # Output: 'B13'
