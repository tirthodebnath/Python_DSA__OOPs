#remove all the vowel from sting
def vowel(string):
    v = ['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in v:
            string = string.replace(i,'')
    print(string)
    return string
string = input("Enter a string: ")
vowel(string)            