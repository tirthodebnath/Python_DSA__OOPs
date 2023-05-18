##2nd largest   element

def find_second_largest(numbers):
    # Initialize variables to store the largest and second largest numbers
    largest = float('-inf')
    second_largest = float('-inf')

    # Iterate through the numbers
    for num in numbers:
        # If the current number is larger than the largest number,
        # update both the largest and second largest numbers
        if num > largest:
            second_largest = largest
            largest = num
        # If the current number is smaller than the largest number but larger
        # than the second largest number, update only the second largest number
        elif num > second_largest and num < largest:
            second_largest = num

    # Return the second largest number
    return second_largest


# Test the function
num_list = [100, 5, 7, 2, 8, 15]
second_largest_num = find_second_largest(num_list)
print("The second largest number in the list is:", second_largest_num)
