##Count and show duplicates
my_list = [1, 2, 2, 3, 4, 4, 5, 4, 3]

duplicates = []
c = {}

for i in my_list:
    if i in c:
        c[i] += 1
        if i not in duplicates:
            duplicates.append(i)
    else:
        c[i] = 1

print("Duplicate elements:", duplicates)
print("Count of each duplicate element:", c)
