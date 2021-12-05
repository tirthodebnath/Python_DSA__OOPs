#Palindrome a sring........1st
def reverse(string):
    reverse_string=""
    for i in string:
        reverse_string=i+reverse_string
    if reverse_string==string:
        print(string,"is palindrome")
    else:
        print(string,"is not palindrome")    

string=input("Enter the string:")
reverse(string)       

#Palindrome a sring........2nd
string=input("Enter the string:")
rev_string=string[::-1]
if string==rev_string:
    print(string,"is palindrome.")
else:
    print(string,"is not palindrome.")    