#20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str):
        stack=[]
        dict={')':'(', '}':'{',']':'['}
        for i in s:
            if i in dict:
                if stack and stack[-1] == dict[i]:
                    stack.pop() 
                else: 
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        
print(Solution().isValid("()[]{}"))        