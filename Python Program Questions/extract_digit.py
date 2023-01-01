#extract digits from a givin string
n=input("Enter a string:")
for i in n:
    if i.isdigit():
        print(i)
    else:
        print("No Digit")
    