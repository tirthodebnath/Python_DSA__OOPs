#Factorial of a number......
# import math 

# n=int(input("Enter the number:"))
# result = math.factorial(n)
# print("factorial of",n,"is:" ,result)


# #Factorial using for loop.....
n=int(input("Enter the number:"))
result=1
for i in range(1,n+1):
    print(i)
    result=result*i

print("Factorial of",n,"is",result)


###Factorial using recustion
# def factorial(n):
#     # Base case: factorial of 0 is 1
#     if n == 0:
#         return 1
    
#     # Recursive case: calculate factorial of n by multiplying it with factorial of (n-1)
#     return n * factorial(n - 1)


# # Test the function
# num = int(input("Enter a number: "))
# result = factorial(num)
# print("Factorial of", num, "is", result)


