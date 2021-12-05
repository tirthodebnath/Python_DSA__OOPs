#Remove Duplicates from list using for loop
list1 = [1,2,3,4,5,6,7,8,9,10,5,3,2,2,4,3,100,123,121]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)