##How to find the sum of digits of a positive integer number using recursion?

def sum(n):
    assert n>=0 and int(n) == n,'n must be a non-negative integer'
    if n ==0:
        return 0
    else:
        return int(n%10) + sum(n//10)

print(sum(30))
