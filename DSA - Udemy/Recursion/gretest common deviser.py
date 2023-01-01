## How to find the gcd(gretest common deviser) of two numbers using recursion?

def gcd(a,b):
    if a<0 and b<0:
        a= -1* a
        b= -1* b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(14,8))
