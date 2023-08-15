##Find the missing number in list
mynum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30]

def fin_missing(list,i):
    sum1=30*31/2
    sum2=sum(list)
    print(sum1-sum2)

fin_missing(mynum,30)