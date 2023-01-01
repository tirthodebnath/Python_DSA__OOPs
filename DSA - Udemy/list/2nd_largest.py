##2nd largest   element

a=[30,10,3,5,6,100,2,40]
target=a[0]

for i in range(0,len(a)-1):
    if target < a[i]:
        target=a[i]
    temp=a[0]
    a[0]=a[i]
    # print(a[0])
    a[i]=temp
print(a)
target1=a[1]
print("Largest Element:",target)
print("2nd Largest Element:",target1)