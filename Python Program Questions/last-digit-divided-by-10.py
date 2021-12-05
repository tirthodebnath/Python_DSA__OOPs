#Check if the number formed by the last digits of N is divide by 10 or not.
def is_divisible(arr,n):    
    last_digit = arr[n-1] %10 

    if last_digit == 0:
        return True
    
arr = [12,345,2,6,70]
n = len(arr)

if (is_divisible(arr,n)):
    print("Yes")
else:
    print("No")
