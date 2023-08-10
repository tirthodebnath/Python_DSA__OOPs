##Python Program to Find Largest Number in a List

##First Method
# a=[]
# n=int(input("Enter number of elements:"))
# for i in range(1,n+1):
#     b=int(input("Enter element:"))
#     a.append(b)
# a.sort()
# print("Largest element is:",a[n-1])


##2nd Method
a=[9,5,6,4,78,45,55,1,22,5,99]
b=a[0]

for i in a:
    if i> b:
        b=i
print(b) 