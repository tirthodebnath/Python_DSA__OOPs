##Show duplicates
my_list = [1, 2, 2, 3, 4, 4, 5, 4,3]

duplicates = []
b = set()
c={}

for i in my_list:
    if i in b and i not in duplicates:
        duplicates.append(i)      
    else:
        b.add(i)

for i in my_list:
    if i not in b:
        c[i] += 1
    else:
        c[i]=1
        
print(duplicates)
print(c)

