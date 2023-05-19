##Python Program to Check Whether a Given Number is Even or Odd using Recursion

def is_even(number):
    # Base cases
    if number == 0:
        return True
    elif number == 1:
        return False
    # Recursive case
    else:
        # Subtract 2 from the number and call the function recursively
        return is_even(number - 2)

print(is_even(101))