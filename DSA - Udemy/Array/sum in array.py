##Given an array of integers nums and an integer target, 
##return indices of the two numbers such that they add up to target
def sum1(array,target):
    for i in range(1,len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                print(i,j)

array=[1,2,3,4,5,6,7,8,9,9,10,10,11,12,13,14,15]
sum1(array,10)