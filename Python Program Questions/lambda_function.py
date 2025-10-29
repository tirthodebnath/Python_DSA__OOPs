##Lambda Function


#Add 10 to every element
# a= lambda x: x+10
# print(a(10))

#Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.
# def func_compute(n):
#  return lambda x : x * n
# result = func_compute(2)
# print("Double the number of 15 =", result(15))

##Write a Python program to sort a list of tuples using Lambda.
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[0])
# print("\nSorting the List of Tuples:")
# print(subject_marks)


############################################################################
##Find the even and odd numbers for the list using lambda functions

numbers = [1, 2, 4, 1, 5, 6, 7, 10, 19]

even_numbers =list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Test")