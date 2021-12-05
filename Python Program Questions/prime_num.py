#Check prime number or not
n=int(input("Enter the number:"))

if(n%2==0):
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")    


#Check prime number or not between 10 to 100
for i in range(10,100):
    if(i%2 != 0):
      print(i,"is a prime number")
       
    