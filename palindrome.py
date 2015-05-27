def palindrome(str):
    strrev= str[::-1]
    a = ""
    if str == strrev:
        a = "palindrome"
    else: 
        a = "not palindrome"
    return a
