#125. Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=''
        for i in s:
            if i.isalnum():
                final=final + i.lower()

        n=len(final)
        l=0
        r=n-1

        while l<r:
            if final[l]!=final[r]:
                return (False)
            l+=1
            r-=1
        return True                

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))   