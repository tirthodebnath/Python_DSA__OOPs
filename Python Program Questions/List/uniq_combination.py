##Python program to get all unique combinations of two Lists
import time

import itertools
from itertools import product

list_1 = ["b", "c", "d"]
list_2 = [1, 4, 9,1]

unique_combinations = []
new_comb=[]

start = time.perf_counter()
print(start)
for i in range(len(list_1)):
	for j in range(len(list_2)):
		unique_combinations.append((list_1[i], list_2[j]))

print(unique_combinations)

for k in unique_combinations:
    if k not in new_comb:
        new_comb.append(k)

end = time.perf_counter()

print("elapsed = ", end-start)


print(new_comb)

start1 = time.perf_counter()

# python program to demonstrate
# unique combination of two lists
# using zip() and permutation of itertools

# import itertools package
import itertools
from itertools import permutations

# initialize lists
list_1 = ["a", "b", "c","d"]
list_2 = [1,4,9]

# create empty list to store the
# combinations
unique_combinations1 = []

# Getting all permutations of list_1
# with length of list_2
permut = itertools.permutations(list_1, len(list_2))

# zip() is called to pair each permutation
# and shorter list element into combination
for comb in permut:
	zipped = zip(comb, list_2)
	unique_combinations1.append(list(zipped))

# printing unique_combination list
print(unique_combinations)

   
end1 = time.perf_counter()

print("elapsed = ", end1-start1)


