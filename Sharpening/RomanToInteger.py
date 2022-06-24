# leetcode: https://leetcode.com/problems/roman-to-integer/


def romanToInt(s: str) -> int:
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s)-1):
        curr_letter = s[i]
        next_letter = s[i+1]
        last_letter = s[-1]

        curr_value = d[curr_letter]
        next_value = d[next_letter]
        last_value = d[last_letter]
        
        if curr_value < next_value:
            total = total - curr_value
        else:
            total = total + curr_value
    
    total = total + last_value
    
    return total

s = "XIV"
print(romanToInt(s))