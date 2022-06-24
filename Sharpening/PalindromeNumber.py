# leetcode: https://leetcode.com/problems/palindrome-number/

# Approaches:
# 1. create two lists of digits, one reversed and check equality.
# 2. stringify the number, reverse the string, and check equality.

def isPalindrome(x: int) -> bool:
    a = str(x)
    b = a[::-1]

    if a == b:
        return True
    else:
        return False

x = 2322

res = isPalindrome(x)
print(res)