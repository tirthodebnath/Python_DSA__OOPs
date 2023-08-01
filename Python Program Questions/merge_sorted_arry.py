##Output: [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6] 
lst1= list(nums1+nums2)
print(lst1)

for i in lst1:
    if i == 0:
        lst1.remove(0)
print(sorted(lst1))





