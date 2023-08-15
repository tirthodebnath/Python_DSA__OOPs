#Write a function which takes a string and returns the count of the carecters 

char_input = "Tirhto is good"

def count_char(char_input):
    b=0
    c=0
    list1= []
    for i in char_input:
        if i ==" ":
            c=c+1
        else:
            b=b+1
    return b,c
            
a,d=(count_char(char_input))
print("Total no of words and space is:",a, "&", d)






