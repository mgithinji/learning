# leetcode: https://leetcode.com/problems/valid-parentheses/

# Approach:

# iterate through 's' and store left-hand parens in a list 'memo'
# when you encounter right-hand paren, .pop() memo list and check for match
# ensure that memo list is empty after iteration

def isValid(s: str) -> bool:
    d = {'(': ')', '{': '}', '[': ']'}
    
    l = len(s)
    
    # odd number of chars, missing pair
    if l % 2 != 0:
        return False

    # temp list to store left-hand parens
    memo = []

    # iterating through str, paren by paren
    for paren in s:
        # left-hand parens get added to memo
        if paren in d.keys():
            memo.append(paren)
        
        # right-hand parens are checked against last left-side bracket in memo, if not empty
        elif len(memo) == 0 or d[memo.pop()] != paren:
            return False

    # if memo is not empty, left-side paren(s) missing a right-hand pair(s)
    if len(memo) > 0:
        return False

    # if all checks pass, paren string is valid
    return True

s = "){"
print(isValid(s))