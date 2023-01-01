# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
print(Solution().isAnagram("anagram","nagaram"))