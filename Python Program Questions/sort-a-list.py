#sort a list assending order
list = [1,2,3,4,5,6,7,8,9,10,5,3,2,2,4,3]
list.sort()
print(list)

#sort a list desending order
list.sort(reverse=True)
print(list)


#sort a list without using sort()
list1 = [1,2,3,4,5,6,7,8,9,10,5,3,2,2,4,3]
new_list = []
while list1:
    minimum = list1[0]
    for i in list1:
        if i > minimum:
            minimum = i
    new_list.append(minimum)
print("after",new_list)        



#sort without using sort() and without duplicates
list1 = [1,2,3,4,5,6,7,8,9,10,5,3,2,2,4,3,100,123,121]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
list2.sort()
#list2.sort(reverse=True) for desending order
print(list2)