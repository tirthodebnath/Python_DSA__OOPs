#168. Excel Sheet Column Title
#https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self,columnNumber):
        result = ""
        while columnNumber > 0:
            result = chr((columnNumber-1)%26 + ord('A')) + result
            columnNumber = (columnNumber-1)//26 
        return result

Solution().convertToTitle(10)
 


        