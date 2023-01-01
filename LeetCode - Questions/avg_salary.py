#1491. Average Salary Excluding the Minimum and Maximum Salary
#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self,salary):
        salary=[]
        max_salary = max(salary)  
        min_salary = min(salary)
        
        salary_sum = 0
        count = 0
        for s in salary:
            if s != min_salary and s != max_salary:
                salary_sum += s
                count += 1
        return salary_sum / count

print(Solution().average([4000,3000,1000,2000]))