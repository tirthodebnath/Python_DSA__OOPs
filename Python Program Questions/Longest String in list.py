#Longest String in list
#https://www.geeksforgeeks.org/python-longest-string-in-list/

test_list = ['gfg', 'is', 'best', 'for', 'geeks', 'Tirthankar']

max = 0

for i in test_list:
    if len(i)>max:
        max= len(i)
        res= i

print("Longest String:" + res)

print(max)




