# ##Fibonacci

def fibonacci(n):
    ##assert n>=0 and int(n) == n,'n must be a non-negative integer'
    if n in [0,1]:
        return n
    else:    
        return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(30))


# class Solution:
#     def fib(n):
#         if n in [0,1]:
#             return n
#         else:
#             return Solution.fib(n - 1) + Solution.fib(n - 2)    

# cls=Solution()
# print(cls.fib(4))