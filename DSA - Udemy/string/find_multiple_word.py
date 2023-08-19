##find how many times given word repeated in the sentence
input = 'big data is booming,data is new oil'
word='data'

input= input.replace(",",' ')
lst= input.split(" ")
count=0
for i in lst:
    if i==word:
        count+=1

print(count)
        

