##Write a python program to find all pairs of integers whose sum is equal to the target.

def add_int(list1, target):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i] == list1[j]:
                continue
            elif list1[i] + list1[j] == target:
                print(list1[i],list1[j])

list1 = [1,2,3,4,5,6,3,2,2]
print(add_int(list1,10)) 