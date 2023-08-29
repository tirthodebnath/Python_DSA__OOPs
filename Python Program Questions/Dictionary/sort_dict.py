#Sort 
# d = {"a": 2, "b": 4, "c": 3, "d": 1, "e": 0}
# print(sorted_dict_keys = dict(sorted(d.items(), key=lambda x: x[0])))


# ##Dictionary
# color_dict = {'red':'#FF0000',
#             'green':'#008000',
#             'black':'#000000',
#             'white':'#FFFFFF'}

##Dictionary
color_dict = {"c": 3, "b": 4,  "d": 1,"a": 2, "e": 0}

# print(dict(sorted(color_dict.keys())))

print(dict(sorted(color_dict.items())))

##Dict Keys
print("Dict Keys =",color_dict.keys())

##Dict Values
print("Dict Values =",color_dict.values())

##Sorted by Keys
print("Sorted by Keys =",sorted(color_dict))

##Sorted by Values
print("Sorted by Values =",sorted(color_dict.values()))


##Sorted the dictionary by keys
print("Sorted the dictionary by keys =",sorted(color_dict.items()))

##Sorted the dictionary by values
sorted_dict = dict(sorted(color_dict.items(), key=lambda item: item[1]))
print("Sorted the dictionary by values =",sorted_dict)




