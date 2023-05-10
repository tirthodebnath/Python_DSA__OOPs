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



    