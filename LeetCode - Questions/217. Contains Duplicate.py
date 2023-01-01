#217. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        self.nums=[]
        counter = []
        
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True
        return False

S=Solution()
