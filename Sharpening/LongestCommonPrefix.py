# leetcode: https://leetcode.com/problems/longest-common-prefix/

# approach:
# 1. start with full first string as longest common prefix, 
#    reduce length as you go through list of strings

def longestCommonPrefix(strs) -> str:
    # empty list returns nothing
    if len(strs) == 0:
        return ""
    
    # first string will be initial common prefix
    res = strs[0]

    # iterate through list and remove chars from initial 'res' until list is complete
    for string in strs:
        
        # quit loop if prefix is empty already
        if res == "": 
            return res

        pre = res
        pre = pre[0:len(string)]

        while len(pre) > 0 and not string.startswith(pre):
            pre = pre[:-1]
        res = pre
    
    return res

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))