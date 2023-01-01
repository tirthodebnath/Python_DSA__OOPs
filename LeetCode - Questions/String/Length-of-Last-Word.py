#58. Length of Last Word
#https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1,0
        while s[i] == " ":
            i = i-1
        while i >= 0 and s[i] !=" ":
            length =length+1
            i =i-1
        return length    
            
print(Solution().lengthOfLastWord("Tirthankar Debnath"))       