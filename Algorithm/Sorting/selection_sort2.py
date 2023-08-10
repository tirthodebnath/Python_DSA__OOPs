# sorting the list using for loop and without using builtin function like min()

list1=[1,2,4,2,3,3,77,4,33,99]
print("Unsorted list:",list1)

for i in range(len(list1)):
    min_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j]<min_val:
            min_val=list1[j]

    min_ind= list1.index(min_val,i)
    if list1[i] != min_val:
        list1[i],list1[min_ind]=list1[min_ind],list1[i]        

print("Sorted list:",list1)