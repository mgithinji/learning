
    
def contains_invalid_chars(s: str) -> bool:
    s = s.lower()
    elems = ['e', '+', '-', '.']
    
    for char in s:
        if char.isdigit() or char in elems:
            continue
        else:
            return True
    
    return False
    
def is_dec(s: str) -> bool:
    
    if '.' in s:
        if s.count('.') > 1:
            return False
    num_exists = False
    for val in s:
        if val.isdigit():
            num_exists = True
    if not num_exists:
        return False
        
    
    sign_elems = ['+', '-']
    if any(x in s for x in sign_elems):
        # sign up front
        signs = {} # {sign, index}
        for i in range(len(s)):
            if s[i] in sign_elems:
                if s[i] in signs:
                    return False
                signs[s[i]] = i
        print(signs)
        # if there's more than one sign
        if len(signs) > 1:
            return False
    
        # if the sign is not in front
        if len(signs) == 1:
            if list(signs.values())[0] != 0:
                return False
    
    return True
    
def is_int(s: str) -> bool:
    if '.' in s:
        return False
    
    num_exists = False
    for val in s:
        if val.isdigit():
            num_exists = True
    if not num_exists:
        return False

    sign_elems = ['+', '-']
    if any(x in s for x in sign_elems):
        # sign up front
        signs = {} # {sign, index}
        for i in range(len(s)):
            if s[i] in sign_elems:
                if s[i] in signs:
                    return False
                signs[s[i]] = i
        print(signs)
        # if there's more than one sign
        if len(signs) > 1:
            return False
    
        # if the sign is not in front
        if len(signs) == 1:
            if list(signs.values())[0] != 0:
                return False
    
    return True
    
def isNumber(s: str) -> bool:
    s = s.lower()
            
    # length of string
    n = len(s)
    
    # check for empty string
    if n == 0:
        return False
    
    # check for invalid characters in s
    if contains_invalid_chars(s):
        return False
    
    
    # when there's an 'e' in the string
    if 'e' in s:
        # when there's more than one 'e'
        if s.count('e') > 1:
            return False
        
        # when 'e' starts or ends the string
        if s.index('e') == 0 or s.index('e') == n - 1:
            return False
        
        # split the left and right sides of 'e'
        ix_e = s.index('e')
        le = s[:ix_e]
        re = s[ix_e+1:]

        print('L: {}'.format(le))
        print('R: {}'.format(re))
        
        if is_dec(le) and is_int(re):
            return True
        else:
            return False
        
    else:
        if is_dec(s) or is_int(s):
            return True
        else:
            return False
            
print(isNumber('-E7'))