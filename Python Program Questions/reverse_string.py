#Reverse a sring........
def reverse(string):
    reverse_string=""
    for i in string:
        reverse_string=i+reverse_string
    print("Reverse string is:", reverse_string)

string=input("Enter the string:")
reverse(string)       