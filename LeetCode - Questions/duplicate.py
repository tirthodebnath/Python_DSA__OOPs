#217. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        nums_set= set(nums)
        if nums != nums_set:
            return True
        else:
            return False
print(Solution().containsDuplicate([1,2,3,1])) 