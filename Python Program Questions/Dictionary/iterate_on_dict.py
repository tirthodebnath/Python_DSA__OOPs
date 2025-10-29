#Iterate over dictionaries using for loops

# d = {'x': 10, 'y': 20, 'z': 30} 
# for dict_key, dict_value in d.items():
#     print(dict_key,'->',dict_value)



# Square of a range of items
# x=5
# d={}

# for i in range(1,x+1):
#     d[i]= i*i
# print(d)

# #Sum of all elements in dictionary
# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))

  
x=100
d=[]

for i in range(1,x+1):
    if i % 2 != 0:
        d.append(i)
print(d)