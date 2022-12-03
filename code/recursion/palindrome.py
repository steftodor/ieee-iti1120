# palindrome recursion example

def palindrome(s):
    if(len(s) == 0):
        return True
    # get the first and last character
    a = s[0]
    b = s[len(s)-1]
    # If the first and last character are the same, cal palindrome again with the first and last digit are removed
    if (a == b):
        return palindrome(s[1:len(s)-1])

    else:
        return False
    


print(palindrome("12321"))
print(palindrome("13321"))
print(palindrome("1"))
print(palindrome("abcabc"))
print(palindrome("abccba"))


