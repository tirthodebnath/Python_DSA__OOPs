#Bubble sorting
list1=[3,5,7,9,3,5,1,2,0]
print("Before sorting:",list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print("After sorting:",list1)    