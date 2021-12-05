#Amstrong number
#1st method ..........................

for i in range(1001):         
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num) 


#2nd method ..........................

n=int(input("Enter the number:"))
sum=0
order=len(str(n))
copy_n=n
while(n>0):
    digit = n%10
    sum= sum + digit**order
    n= n//10
if(sum==copy_n):
    print(f"{copy_n} is a armstrong number")
else:
    print(f"{copy_n} is not a armstrong number")        





