##Write a Python code to accept a string and count the number of vowels and consonants.

sentence = "aeiBCD"
vow=0
con=0
for i in sentence:
    if i in "aeiouAEIOU":
        vow=vow+1
    elif i not in "aeiouAEIOU":
        con=con+1
print(vow,con)