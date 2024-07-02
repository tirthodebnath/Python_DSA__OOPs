#1. Two Sum
#https://leetcode.com/problems/two-sum/

#1st method
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)



#2nd
    # complement=dict()
    # for i in range(len(nums)):
    #     num= nums[i]
    #     complement2 = target - num

    #     if num in complement:
    #         return [complement2[num], i]
    #     else:
    #         complement[complement] = i    