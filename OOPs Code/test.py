# def recussion(n):
#     if n<1:
#         print("n is big")
#     else:
#         recussion(n-1)
#         print(n)
    
# recussion(5)

# a = range(1,10000)
  
# # initializing a with xrange()
# x = xrange(1,10000)
  
# # testing the type of a
# print ("The return type of range() is : ")
# print (type(a))
  
# # testing the type of x
# print ("The return type of xrange() is : ")
# print (type(x))

########################################

# ********DAY 19********
# Python coding question:

# BLACKJACK: Given three integers between 1 and 11,
# if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


# I will be posting a coding question every day for daily revision.
# Pour in your answers!




a=input("Enter:",)
b=input("Enter:",)
c=input("Enter:",)
d=a+b+c
f=d-10
if d == 21:
    print("True")
elif d > 21 and a or b or c or d ==11 and f > 21:
    print("Bust")


    


