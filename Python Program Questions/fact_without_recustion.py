##Factorial without recustion...
def factotail(n):
    if n == 0:
        return 0
    
    fact = 1
    
    for i in range(1,n+1):
        fact = fact*i    
    return fact

a= 123
digit_sum=0

##Converting string to int
for j in str(a):
    digit= int(j)
    digit_factorial=factotail(digit)
    digit_sum = digit_sum+digit_factorial

print(digit_sum)
