##Creating array in python

from array import *

arr1= array('i',[1,2,3,4,5,6,7,8,9,0])

# # print(arr1)

# ##Inserting in the array

# arr1.insert(0,9)
# print(arr1)

##Traversing the array

def traverse(arr):
    for i in range(len(arr)):
        print(arr[i])
traverse(arr1)        