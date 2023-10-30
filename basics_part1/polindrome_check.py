def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

    # Additional condition for odd-length strings
    if left == right:
        return True

