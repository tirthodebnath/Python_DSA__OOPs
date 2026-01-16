# Problem:
# Write a Python function that takes a list of numbers
# and returns the largest number without using max().

# lst = [3, 7, 2, 9, 4]
# a = lst[0]

# for i in range(1, len(lst)):
#     if a < lst[i]:
#         a = lst[i]

# print(a)


# Problem:
# Write a Python function to count the frequency of each character 
# in a string without using Counter or any built-in frequency functions.

# Input= "aabbbc"
# a = {}

# for i in Input:
#     if i in a:
#         a[i] += 1
#     else:
#         a[i] = 1

# print(a)


# Problem:
# Write a Python function that finds the 
# second largest number in a list without using sort() or max().

# lst = [10, 5, 8, 20, 15]

# for i in range(len(lst)):
#     for j in range(i+1, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]

# print(lst[-2])


##Problem:
# Write a Python function to find the missing number in a list.

# a = [3, 0, 1]

# n = len(a)
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(a)

# missing = expected_sum - actual_sum
# print(missing)   # 2
