# a = [1, -12, 10, 45, -9, 4, 6, 0, -59]

# # Initialize variables to store the closest sum and the corresponding pair of elements
# closest_sum = float('inf')
# closest_pair = None

# # Iterate over each pair of elements
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         # Calculate the sum of the current pair
#         current_sum = a[i] + a[j]
        
#         # Check if the current sum is closer to zero than the previous closest sum
#         if abs(current_sum) < abs(closest_sum):
#             closest_sum = current_sum
#             closest_pair = (a[i], a[j])

# # Print the closest sum and the corresponding pair of elements
# print(f"The closest sum to zero is {closest_sum} with the pair {closest_pair}.")


###########################################################################################


