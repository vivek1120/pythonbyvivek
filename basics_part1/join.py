def is_palindrome(s):
    # Step 1: Remove non-alphanumeric characters and spaces
    s = ''.join(e for e in s if e.isalnum())
    
    # Step 2: Convert to lowercase
    s = s.lower()
    
    # Step 3: Check if the string is the same when reversed
    return s == s[::-1]

