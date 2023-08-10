'''Selection sort is a sorting algorithm that works by repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.'''

##Using builtin function

list1=[5,3,6,6,2,7,10,7,9]

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val, i)   # sorting of duplicate values
    list1[i],list1[min_ind] = list1[min_ind],list1[i]
print(list1)  