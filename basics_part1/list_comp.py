def is_palindrome(s):
    # Step 1: Remove non-alphanumeric characters and spaces
    s = ''.join(e for e in s if e.isalnum())
    
    # Step 2: Convert to lowercase
    s = s.lower()
    new = s.lower()
    
    # Step 3: Check if the string is the same when reversed
    return s == new[::-1]

        

print(is_palindrome("modom"))


