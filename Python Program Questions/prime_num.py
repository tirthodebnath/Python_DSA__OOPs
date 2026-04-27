# #Check prime number or not
# n=int(input("Enter the number:"))

# if(n%2==0):
#     print(n,"is not a prime number")
# else:
#     print(n,"is a prime number")    


#Check prime number or not between 10 to 100
cont = 0
d = []
for num in range(10, 14):   # start from 10, go up to 100
    print(num)
    if num > 1:
        for i in range(2, num):
            print(i)
            if num % i == 0:
                break
    else:
        print(num)
        cont += 1    # move inside the 'else', so count only primes
print("Total prime numbers between 10 and 100:", cont)

