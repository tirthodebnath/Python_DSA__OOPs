##Sort 
# d = {"a": 2, "b": 4, "c": 3, "d": 1, "e": 0}
# print(sorted_dict_keys = dict(sorted(d.items(), key=lambda x: x[0])))


##Sort by key
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

print(dict(sorted(color_dict.items())))

##Dict Keys
print(color_dict.keys())

##Dict Values
print(color_dict.values())

##Sorted by items
print(sorted(color_dict.items()))

##Sorted by items
print(sorted(color_dict.values()))

##Sorted by items
print(sorted(color_dict))
