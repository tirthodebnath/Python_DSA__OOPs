#1st approach.....for finding maximum and minimum number 
arr=[3,2,1,56,10000,167]

max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]


max=arr[n-1]
print("the maximun eliment is:", max)

min=arr[0]

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print("the minimum element is:",min) 


##Currect One

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# arr = [3, 2, 1, 56, 10000, 167]
# bubble_sort(arr)
# print("Max = ", arr[-1])
# print("Min = ", arr[0])
# print(arr)
      


