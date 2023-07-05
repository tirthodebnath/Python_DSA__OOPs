#217. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(nums,counter):
        nums=[]
        counter = []
        
        for num in nums:
            if num not in counter:
                counter.append(num)
            else:
                return True
        return False

S = Solution()
nums = [1, 2, 3, 4, 5, 1]  # Example list of numbers
print(S.containsDuplicate(nums))

