# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            char1, char2 =s[i], t[i]
            if char1 not in d:
                if char2 in d.values():
                    return False
                    d[char1] = char2
                elif d[char1] != char2:
                    return False

print(Solution().isIsomorphic("egg","add"))            
            