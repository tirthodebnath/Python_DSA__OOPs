# #Check prime number or not
# n=int(input("Enter the number:"))

# if(n%2==0):
#     print(n,"is not a prime number")
# else:
#     print(n,"is a prime number")    


#Check prime number or not between 10 to 100
cont = 0
for num in range(10, 101):   # start from 10, go up to 100
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            cont += 1    # move inside the 'else', so count only primes

print("Total prime numbers between 10 and 100:", cont)

