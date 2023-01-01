#1523. Count Odd Numbers in an Interval Range
#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

#By me
low=3
high=7
def count():
    count1=[]
    for i in range(low,high+1):
        if i%2!=0:
            count1=count1+[i]
    return len(count1)
print(count())

#Accepted one
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0:
            if high % 2 != 0:
                return (high - low) // 2 + 1
            else:
                return (high - low) // 2 + 1
        else:
            if high % 2 != 0: 
                return (high - low) // 2 + 1
            else: 
                return (high - low) // 2