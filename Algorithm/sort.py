#Selection sort
list1=[1,4,6,2,5,3,13,31]

min_val= min(list1)
min_index=list1.index(min_val)
for i in range(len(list1)):
    if list1[i]<min_val:
        min_val=list1[i]       
print(list1)
