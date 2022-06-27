# leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: list) -> list:
    nums_set = set(nums)
    d = len(nums) - len(nums_set)
    placeholders = ['_'] * d
    
    return list(nums_set) + placeholders

nums = [1,1,2]
print(removeDuplicates(nums))