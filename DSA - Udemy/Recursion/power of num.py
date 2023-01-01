## How to calculate power of a number using recursion?

def power(base,power1):
    assert power1>=0 and int(power1) == power1,'base must be a non-negative integer'
    if power1 == 0:
        return 1
    if base == 1:
        return base
    return base * power(base,power1-1)

print(power(2,3))