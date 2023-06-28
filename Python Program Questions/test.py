# Python code to convert string to list
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

##Longest string from the list

# str_list = ["jbcjb", "hgcs", "dvgvcsdjs", "sjvdwvhjc"]
# longest_str = ""

# for i in str_list:
#     if len(i) > len(longest_str):
#         longest_str = i

# print("Longest string:", longest_str)
       

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

# Find the max consecutive ones in the given list
# L=[1,2,1,1,1,1,4,5,1,1,3,4,1,1,1] in python  

# def max_consecutive_ones(lst):
#     max_ones = 0
#     current_ones = 0

#     for num in lst:
#         if num == 1:
#             current_ones += 1
#             max_ones = max(max_ones, current_ones)
#         else:
#             current_ones = 0

#     return max_ones

# L = [1, 2, 1, 1, 1, 1, 4, 5, 1, 1, 3, 4, 1, 1, 1]
# max_ones = max_consecutive_ones(L)
# print("Maximum consecutive ones:", max_ones)

#############################################################

# test = {"a": 7, "b": 4, "c": 1}

# sorted_dict = dict(sorted(test.items(), key=lambda x: x[1]))

# print(sorted_dict)

##########################################################

numbers = [1, 2, 4, 1, 5, 6, 7, 10, 19]

even_numbers = lambda x: x % 2 == 0, numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)





 