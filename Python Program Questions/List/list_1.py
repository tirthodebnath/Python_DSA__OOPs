# Find the max consecutive ones in the given list
# L=[1,2,1,1,1,1,4,5,1,1,3,4,1,1,1] in python  

def max_consecutive_ones(lst):
    max_ones = 0
    current_ones = 0

    for num in lst:
        if num == 1:
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0

    return max_ones

L = [1, 2, 1, 1, 1, 1, 4, 5, 1, 1, 3, 4, 1, 1, 1]
max_ones = max_consecutive_ones(L)
print("Maximum consecutive ones:", max_ones)