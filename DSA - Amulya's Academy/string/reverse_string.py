# Reverse string  
# Using a while loop  
  
str = "JavaTpoint" #  string variable  
print ("The original string  is : ",str)   
reverse_String = ""  # Empty String  
count = len(str) # Find length of a string and save in count variable  
while count > 0:   
    reverse_String += str[ count - 1 ] # save the value of str[count-1] in reverseString  
    count = count - 1 # decrement index  
print ("The reversed string using a while loop is : ",reverse_String)# reversed string  