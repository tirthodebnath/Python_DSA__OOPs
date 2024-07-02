#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    # Base condition
    if x < 0:
        return False
    # Store the number in a variable
    number = x
    # This will store the reverse of the number
    reverse = 0
    while number:
        reverse = reverse * 10 + number % 10
        number //= 10
    return x == reverse