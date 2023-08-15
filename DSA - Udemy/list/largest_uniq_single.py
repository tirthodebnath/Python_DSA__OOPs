#Largest uique single number
lst = [8, 8, 3, 3, 1, 4, 5, 6]
non_repeated = []

for num in lst:
    if lst.count(num) == 1:
        non_repeated.append(num)

print(max(non_repeated))

print("Non-repeated numbers:", non_repeated)