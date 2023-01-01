# def f3(n):
#     if n <= 0:
#         return 1
#     else:
#         return 1 + f3(n/5)
# print(f3(5))        


#######################################################
# def f4(n,m,o):
#     if n<=0:
#         print(n,m,o)
#     else:
#         f4(n-1,m+1,o)
#         f4(n-1,m,o+1)

# print(f4(5,1,2))
#######################################################
# def foo(array):
#     sum=0
#     product=1

#     for i in array:
#         sum+=i
#         product*=i

#     print("Sum="+str(sum)+", Product="+str(product))    

# foo([1,2,3,4,5])

# #######################################################

# def printPairs(array):
#     for i in array:
#         for j in array:
#             print(str(i)+","+str(j))

# printPairs([1,2,3,4,5])

# #######################################################
# def printPairs(array):
#     for i in range(0,len(array)):
#         for j in range(i+1,len(array)):
#             print(array[i] +","+ array[j])

# printPairs([1,2,3,4,5])



#####################################################################################

# class Solution:
#   def fib(self, N: int) -> int:
#     if N < 2:
#       return N

#     dp = [0, 0, 1]

#     for i in range(2, N + 1):
#       dp[0] = dp[1]
#       dp[1] = dp[2]
#       dp[2] = dp[0] + dp[1]

#     return dp[2]


# number = "12345"
# result = []
# for digit in number:
#     result.append(digit)
# print(result[-1])

# num = 13579
# x = [int(a) for a in str(num)]
# print(x[-1])
#############################################
# def check(num):
#     x = [int(i) for i in str(num)]
#     if x[-1] == 0:
#         print("Zero")

#     if x[-1] == 5:
#         print("Five")

#     if num%2 == 0 and x[-1] != 0:
#         print("Even")

#     if num%2 !=0 and x[-1] != 5:
#         print("Odd")

# print(check(9))                    
#######################################################

#arr=[1,2,3,4,5]

# def check(arr):
#     for i in range(0, len(arr)):
#         if (arr[i] > arr[0]):
#             arr[0] = arr[i]
#     return("MAX=",arr[0])

# print(check([1,2,3,4,5]))

##################################################################

# list1 = [10, 20, 4, 45, 99]
 
# mx = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])

# for i in range(2,len(list1)):
#     if list1[i] > mx:
#         secondmax = mx
#         mx = list1[i]
#     elif list1[i] > secondmax and \
#         mx != list1[i]:
#         secondmax = list1[i]
#     elif mx == secondmax and \
#         secondmax != list1[i]:
#           secondmax = list1[i]
 
# print("Second highest number is : ",\
#       str(secondmax))


#######################################################################

# def f(value, values):
#     v = 1
#     values[0] = 44
#     print(values)
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])
##########################################################

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# for i in range(len(a)):
#     if i %2 == 0:
#         print(a[i])

##################################################

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numToIndex = {}
#         for i, num in enumerate(nums):
#             if target - num in numToIndex:
#                 return numToIndex[target - num], i
#             numToIndex[num] = i

# x = ["ab", "cd", "ef", 48,"gh","ij",9,"kl"]

# y=[]
# for i in x:
#     if(i != 48 and i != 9):
#         y.append(i)
# print(y)




# # make a star piramid

# def star(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end="")
#         print('\r')
    
# star(n=10)

################################################################################



# lan=["ab", "cd", "ef", 48,"gh","ij",9,"kl"]

# for i in lan:
#     if i == 48 or i == 9:
#         continue
#     print(i)

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# def capitalizeWord(str):
#    result=""
#    words = str.split(" ")
#    for word in words:
#       result= result + word[0:1].upper() + word[1:len(str)] + " "
#    return result

# print(capitalizeWord("tirtho"))

# This python program tells if there exists a pair in array whose sum results in x.

# Function to find and print pair

# def chkPair(A, size, x):
   
#    for i in range(1, size):
#       for j in range(i + 1, size):
#          if (A[i] + A[j] == x):
#             print(i,j)
            
# A = [0, -1, 2, -3, 1]
# x = -2
# size = len(A)
# print(chkPair(A,size,-2))

# if __name__ == "__main__":
# 	A = [0, -1, 2, -3, 1]
# 	x = -2
# 	size = len(A)

# 	if (chkPair(A, size, x)):
# 		print("Valid pair exists")

# 	else:
# 		print(f"No valid pair exists for {x}")

# 	# This code is contributed by rakeshsahni

##############################################################

##Find the missing values for a range of values in a list
# a= [1,2,4,5,6,8,10]

# def find(a):
#    return[i for i in range(a[0],a[-1])if i not in a]

# print(find(a))  

##########################################################

##Sum of First N Natural Numbers in Python
# n=int(input("Enter a number: "))
# sum1 = 0
# while(n > 0):
#     sum1=sum1+n
#     n=n-1
# print("The sum of first n natural numbers is",sum1)


## 2nd largest natural number in list

# a=[1,2,3,4,5,6,7,8,9,10,11,12]

# target=a[0]
# target1=a[1]

# for i in a:
#     if target < i:
#         target=i
#         for j in range(1,len(a)):
#             if target1 < j:
#                 target1 = j
# print(target1)

#########################

# b=[]
# c=[]
# def find(a):
#     for i in a:
#         if i ==19:
#             b.append(i)
#     for j in a:
#         if j == 5:
#             c.append(j)

#     if len(b) ==2 and len(c) > 3:
#         return True
#     else:  
#         return False   

# a = [19, 19, 5, 5, 5, 5, 5]
# print(find(a))    

########################################

# str1 = "Salad is healthy snack"
# str1= str1.split(" ")
# def word(str1):
#     for i in str1:
#         if(i[0]=="S" or i[0]=="s"):
#             print(i)
# word(str1)

#######################################


# def func(a, b):
#     for i in range(a,b):
#         if i%3==0 and i%5==0:
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         else:
#             print(i)
# print(func(1,101))                


############################################################
# a=[30,10,3,5,6,100,2]
# target=a[0]

# for i in range(0,len(a)-1):
#     if target < a[i]:
#         target=a[i]
#     temp=a[0]
#     a[0]=a[i]
#     a[i]=temp
# print(a)
# target1=a[1]
# print("Largest Element:",target)
# print("2nd Largest Element:",target1)

#############################################################

##Decorator functions

# def div(a,b):
#     print(a/b)
      
# def smart_div(func):

#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
    
#     return inner

# new_div=smart_div(div)
# new_div(2,4)

############################################

# class sumClass:
#     def sum(self, a, b):
#         print("First method:",a+b)
#     def sum(self, a, b, c):
#         print("Second method:", a + b + c)
        
# obj=sumClass()
# obj.sum(19, 8) #correct output
# # obj.sum(18, 20) #throws error

########################################################################

# str ="naman"
# count= str.count("n")
# # for i in String:
# #     for j in String:
# #         if i == j:
# #             print(i)

# print(count)


##############################################################

# n=int(input("Enter number:"))

# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return (check(n - 2))

# if(check(n)==True):
#       print("Number is even!")
# else:
#       print("Number is odd!")

######################################################

# Given an input string, please print the list of all characters in the string.

# String: “naman”.

# Output: “n=2,a=2,m

###################################################### 

mul = [lambda x: i for i in [0,1,2,3,5]]

print(mul)

p = [m(3) for m in mul]

print(p)

l=[]
for i in mul:
    # print(i)
    l.append(i)
print(l)
