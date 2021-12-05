#14. Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs:[]):
        if len(strs) == 0:
            return("String is empty")

        minlen = len(strs[0])    #Length of the shortest string in the array
        for i in range(len(strs)):
                minlen = min(len(strs[i]),minlen)

        lcp = ""
        i = 0
        while i < minlen:
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return(lcp)

            lcp += char
            i=i+1
        return lcp    

n=Solution()
print(n.longestCommonPrefix(["flower","flow","flight"]))                  