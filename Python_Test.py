# #Python code to convert string to list
# str1 = "The following function would TAKE as input a text string and create a list of all \
# the words in the text each of Which contains only lower-case letters and is of length no \
# longer than 5"
# def Convert(str1):
#     li = list(str1.split(" "))
#     li1=[]
#     for i in li:
#         if len(i)<6 and i.islower():
#             li1.append(i)
#             return li1
        
# print(Convert(str1))

# ##############################################################################################################################

#Longest string from the list

# str_list = ["jbcjb", "hgcs", "dvgvcsdjs", "sjvdwvhjc"]
# longest_str = ""

# for i in str_list:
#     if len(i) > len(longest_str):
#         longest_str = i

# print("Longest string:", longest_str)
       
# #######################################################
# str_list = ["jbcjb", "hgcs", "dvgvcsdjs", "sjvdwvhjc"]

# # Bubble sort based on length (descending)
# for i in range(len(str_list)):
#     for j in range(len(str_list) - 1):
#         if len(str_list[j]) < len(str_list[j + 1]):
#             # swap
#             str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]

# print(str_list)



#We want to design a function to decrypt a piece of text, which has been encrypted with the following scheme:

# a=["The","ram"]
# for i in a:
#     c=i
#     for j in c:
#         print(j) 


# # # #############################################################################################################################

##Show uniq values only

# t="ababab"
# t1=""
# for i in t:
#     if i not in t1:
#         t1+=i
# print(t1)


# text="ababab"
# li=list(text.split(" "))
# li1=[]
# li2=[]
# for i in li:
#     for j in i:
#         if j not in li2:
#             li2+=j
#             print(li2)            


##########################################################################################

# li="This is by no means something specially designed to wear sometimes"
# li1 = list(li.split(" "))
# li2=[]
# for i in li1:
#     if len(i)<=5 and i[-1]=="s":
#         li2.append(i)    
# print(li2) 


#########################################################################################

##Private Protected Public

# class MyClass:
#     __var2 = 'var2'
#     var3 = 'var3'
 
#     def __init__(self):
#         self.__var1 = 'var1'
 
#     def normal_method(self):
#         print(self.__var1)
 
#     @classmethod
#     def class_method(cls):
#         print(cls.__var2)
 
#     def my_method(self):
#         print(self.__var1)
#         print(self.__var2)
#         print(self.__class__.__var2)
 
 
# if __name__ == '__main__':
#     print(MyClass.__dict__['var3'])
 
 
# clzz = MyClass()
# clzz.my_method()

################################################################

# def list_integer(l):
#   list_int = []
#   for i in l:
#     if type(i) is int:
#       list_int.append(i)
#     else:
#       pass
#   if len(list_int)>0:
#     return list_int
#   else:
#     return 'No Integer Present'
# l=[1,2,3,4,5,"td","fd","d"]
# print(list_integer(l))

##################################
##Uniq carectors

# string="zxvczbtxyzvy"

# for i in string:
# 	count=0
# 	for j in string:
# 		if i==j:
# 			count=count+1
# 		if count > 1:
# 			break		
# 	if count == 1:
# 		print(i) 
# print(count)

####################################
##Repetation of string

# str = "Emma is good developer. Emma is a writer"
# str=str.split(" ")
# count=0
# for i in str:
# 	if i =="Emma":
# 		count=count+1
# print(count)	


#######################################

##write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for i in a:
#     if i < 5:
#         print(i)

##########################################


##how to take input in a list in python

# a = []
# s = int(input("Enter the size of array: "))
# for i in range(0, s):
#     elements = int(input("Enter the elements of the array: "))
#     a.append(elements)
# for i in a:
#     if i % 2 == 0:
#         print(i)
# print(a) 


#############################################


## write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c=[]

# for i in a:
#     for j in b:
#         if i==j & i not in c:
#             c.append(i)
# print(c)

##########################################

##Check string is palindrome or not

# strig = str(input("Enter the string: "))
# rev_string = ""

# for i in strig:
#     rev_string = i +rev_string
#     print("Rev String:",rev_string)
# if strig == rev_string:
#     print("Palindrome string")
# else:
#     print("not palindrome string")

#####################################

# #list comprehension function
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([i for i in a if i%2 == 0])


########################################################################
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add("Vicki")
# print(sampleSet) 
# ###############################################################

# ##Input
# a=[1,2,3,4,5,6,7]
# ##Output
# # b=[{4,2},{5,3}..]


# a = [1, 2, 3, 4, 5, 6, 7]
# b = [{x, y} for x, y in zip(a[1::2], a[::2])]
# print(b)  # output: [{2, 4}, {3, 5}, {6, 7}]

###############################################################


# test = {"a": 7, "b": 4, "c": 1}

# sorted_dict = dict(sorted(test.items(), key=lambda x: x[1]))

# print(sorted_dict)

##########################################################

# numbers = [1, 2, 4, 1, 5, 6, 7, 10, 19]

# even_numbers = lambda x: x % 2 == 0, numbers
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)

########################################################

# my_list = ['apple','mango','grape']
# # o/p = ['elppa','ognam','eparg']

# for i in my_list:
#     print(i[::-1])

#######################################################

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

# mul = [lambda x: i for i in [0,1,2,3,5]]

# print(mul)

# p = [m(3) for m in mul]

# print(p)

# l=[]
# for i in mul:
#     # print(i)
#     l.append(i)
# print(l)


######################################################


# import string library function
# import string

# print("Hello")
# # Storing the characters space, tab etc
# result = string.whitespace

# # Printing the values
# print(result)
# print("Geeksforgeeks")


###########################################################

# class someSkunkFunk:
#     def __init__(self,name: str,exp: int,salary: float,hike: float,hike_cycle: int= 1):

#         # Validation
#         assert type(name) == str, f"Name has to be str, received: {type(name)} !"
#         assert type(exp) == int, f"Experience has to be int, received: {type(exp)} !"
#         assert type(salary) == int or type(salary) == float, f"Salary has to be int or float, received: {type(salary)} !"
#         assert type(hike) == int or type(hike) == float, f"Hike has to be int float, received: {type(hike)} !"
#         assert type(hike_cycle) == int, f"Hike Cycle has to be int, received: {type(hike_cycle)} !"
#         assert exp >= 0, f"Experience cannot be negative, parameter received: {exp}."
#         assert salary >= 0, f"Salary cannot be negative, parameter received: {salary}."
#         assert hike >= 0, f"Hike cannot be negative, parameter received: {hike}."
#         assert hike_cycle >= 0, f"Experience cannot be negative, parameter received: {hike_cycle}."

#         # Assigning to self
#         self.name = name
#         self.exp = exp
#         self.salary = salary
#         self.hike = hike
#         self.hike_cycle = hike_cycle

#     def initialSalary(self)->float:
#         return round(self.salary/((1 +(self.hike/self.hike_cycle))**self.exp),2)

# def inSalLst(self):
#         return [self.name,self.initialSalary()]


### Count the vowels

# a="Umbrella"

# v=["a","e","i","o","u","A","E","I","O","U"]

# for i in a:
#     if i in v:
#         print(i)



######################################################
# my_list = {"name": 10, "age": 25, "city": 47}

# print(my_list.sorted())

####################################################

#What will be the output?

# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# print(d['k1'][2]['k2'][1]['tough'][2][0])

#########################################################


# list1 = [1,2,3,4,5,6,3,2,2]

# target=12

# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         for k in range(j+1, len(list1)):
#             if i+j+k== target:
#                 print(i,j,k)
                
#########################################################

##Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
##If the string length is less than 2, return instead of the empty string.
# def str(word):
#     if len(word) < 2:
#         return " "
#     else:
#         return word[0:2] + word[-2:]

# print(str("Tirtho"))

##Get a single string from two given strings, 
# separated by a space and swap the first two characters of each string
# def chars_mix_up(a, b):
#   new_a = a[:1] + b[1:]
#   new_b = b[:1] + a[1:]

#   return new_a + ' ' + new_b
# print(chars_mix_up('abc', 'xyz'))


##Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged

# def add_string(str1):
#   length = len(str1)

#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'

#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))



'''Python Program to Return the Length of the Longest Word from the List of Words'''

# def str(word,target):
#     for i in word:
#         if len(word[i])>len(target):
#             target.append(word[i])
#             return target[i]
# word=["abc","abcd","abcde"]
# target=[]
# print(str(word,target))


# word=["abc","abcd","abcde"]

# print(len(word[2]))

# function to find the longest
# length in the list
# def longestLength(a):
# 	max1 = len(a[0])
# 	temp = a[0]

# 	# for loop to traverse the list
# 	for i in a:
# 		if(len(i) > max1):

# 			max1 = len(i)
# 			temp = i

# 	print("The word with the longest length is:", temp,
# 		" and length is ", max1)


# # Driver Program
# a = ["one", "two", "third", "four"]
# longestLength(a)


# # 2nd method function to find the longest length in the list
# def longestLength(words):
# 	finalList = []
	
# 	for word in words:
# 		finalList.append((len(word), word))
	
# 	finalList.sort()
	
# 	print("The word with the longest length is:", finalList[-1][1],
# 		" and length is ", len(finalList[-1][1]))


# # Driver Program
# a = ["one", "two", "third", "four"]
# longestLength(a)

##Write a Python program to remove the characters which have odd index values of a given string

# def odd_values_string(str):
#   result = "" 
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result

# print(odd_values_string('abcdef'))
# print(odd_values_string('python'))


##Recursion: Sum of a list of numbers

# def sumOfNumbers(list):
#     if len(list)  == 1:
#         return list[0]
#     else:
#         return list[0] + sumOfNumbers(list[1:])

# print(sumOfNumbers([1,2,3,4,5,6,7,8,9]))

# ##FActorial
# def fact(n):
#     if n<=1:
#         return n
#     else:
#         return n * fact(n-1)

# print(fact(10))

##Fibonacci Number

# def fibonacci(n):
#     if n ==1 or n==2:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(9))


# class cal():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
    
#     def add(self):
#         return self.a + self.b
    
#     def sub(self):
#         return self.a - self.b
    
# c=10
# d=10    
# d=cal(c,d)
# print(d.area())

# class rectangle():
#     def __init__(self,breadth,length):
#         self.breadth=breadth
#         self.length=length
#     def area(self):
#         return self.breadth*self.length
# a=int(input("Enter length of rectangle: "))
# b=int(input("Enter breadth of rectangle: "))

# obj=rectangle(a,b)
# print("Area of rectangle:",obj.area())



# x=0
# while(x<5):
#     if(x>3):
#         continue
#         x+=1
#     else:
#         print(x,end="")



################################


# list1 = [15, 18, 2, 36, 12, 78, 5, 6, 9]
# b=0
# for i in list1:
#     b=b+i
#     avg=b/len(list1)
# print(avg)    

################################
# # Input->  a = 1475896
# # Output->  1**7+4**7+7**7+5**7+8**7+9**7+6**7 = 8078110

# a = 1475896
# b =list(str(a))
# c= len(b)
# d=[]
# e=0
# for i in b:
#     if type(i) == str and i not in d:
#         i = int(i)
#         d.append(i)

# for i in d:
#     e = e+i**c
# print(e)    

#######################################


# a = [1,2,4,2,4,2,3]
# Output: [1,"_","_","_", 4,2,3]

# a = [1,2,4,2,4,2,3,3]
# store = {}

# for i in range(len(a)):
#     store[a[i]] = i
# print()
    
# for j in range(len(a)):
#     if store[a[j]] != j:
#         a[j] = "_"

# print(a)


###################################

# logs4 = [
#     ["1", "user_96", "resource_5"],
#     ["1", "user_10", "resource_5"],
#     ["301", "user_11", "resource_5"],
#     ["603", "user_12", "resource_5"],
#     ["301", "user_12", "resource_5"],
  
#     ["1603", "user_12", "resource_7"],
# ]

# # Should return:
# # {
# #  'user_96': [1, 1],
# #  'user_10': [1, 1],
# #  'user_11': [301, 301],
# #  'user_12': [301, 1603],
# # }

# # output = {}

# # for row in logs4:
# #     temp = [] 
# #     if row[1] not in output:
# #         output[row[1]] = list()
    
# #     output[row[1]].append(row[0])
        
# # for key,value in output.items():

# #     if len(value) == 1:
# #         value.append(value[0])
    
# #     else:
# #         sorted(value) 
# #         value = value[0],value[-1]
# #         value = list(value)
# #         print(key, value)
        
# # print(output)
        


#######################################################


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(5))



#####################

# lst = [8, 3, 1, 2, 3, 4, 5, 5, 6, 6, 7, 9, 10]

# # Step 1: remove duplicates manually
# unique = []
# for x in lst:
#     if x not in unique:
#         unique.append(x)

# # Step 2: sort manually (using bubble sort)
# n = len(unique)
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         if unique[j] > unique[j+1]:
#             # swap
#             unique[j], unique[j+1] = unique[j+1], unique[j]
#     # print(i)

# print(unique)

###########################################################

# # define dictionary
# my_dict = {"a": 10, "b": 20, "c": 30, "d": 80}

# def manage_dict(key, value=None):
#     if key not in my_dict:
#         return f"Key '{key}' not found!"
    
#     if value is not None:   # update if value is given
#         my_dict[key] = value
#         return f"Updated: {key} = {my_dict[key]}"
#     else:                   # return current value
#         return f"Current: {key} = {my_dict[key]}"

# # Examples:
# print(manage_dict("a"))        # get value of 'a'
# print(manage_dict("b", 99))    # update 'b' to 99
# print(manage_dict("c"))        # get updated value of 'c'
# print(my_dict)                 # check dictionary


# define dictionary
# my_dict = {"a": 10, "b": 20, "c": 30, "d": 80}

# def manage_dict():
#     key = input("Enter the key (a/b/c/d): ").strip()
    
#     if key not in my_dict:
#         print(f"Key '{key}' not found!")
#         return
    
#     choice = input("Do you want to update the value? (yes/no): ").strip().lower()
    
#     if choice == "yes":
#         value = input(f"Enter new value for '{key}': ").strip()
        
#         # Convert value to int if it's a number
#         if value.isdigit():
#             value = int(value)
        
#         my_dict[key] = value
#         print(f"Updated: {key} = {my_dict[key]}")
#     else:
#         print(f"Current: {key} = {my_dict[key]}")

# # Run continuously until user exits
# while True:
#     manage_dict()
#     cont = input("Do you want to continue? (yes/no): ").strip().lower()
#     if cont != "yes":
#         break

# print("\nFinal Dictionary:", my_dict)

# Find all prime numbers from 1 to 100

# for num in range(2, 101):  # start from 2 (1 is not prime)
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):  # check divisibility up to sqrt(num)
#         print(num)
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, "is a prime number")



# def prime(n):
# 	a = 0
# 	n = list(str(n))
# 	for i in n:
# 		a +=int(i)
# 	return a
# print(prime(1234)) 

##Max profit from stock prices
# prices = [7, 1, 5, 3, 6, 4]

# max_profit = 0

# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         profit = prices[j] - prices[i]
#         if profit > max_profit:
#             max_profit = profit

# print(max_profit)   # 5


# lst = [3, 7, 2, 9, 4]
# a = lst[0]

# for i in range(0,len(lst)):
#     if a < lst[i]:
#         a=lst[i]

# print(a)


# class my_str:
#     def m_str(self, a):
#         b = {}
#         for i in a:
#             if i in b:
#                 b[i] += 1
#             else:
#                 b[i] = 1
#         return b

# s = my_str()
# print(s.m_str("tirtho"))

logs = "1233345566789"
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

result = remove_duplicates(logs)
print(result)
