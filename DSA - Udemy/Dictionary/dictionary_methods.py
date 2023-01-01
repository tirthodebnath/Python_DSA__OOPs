mydict = {'name':"Tirtho", "age":30,"Place":"Kolkata","Education":"M.Tech"}
# mydict["place"] = "Kolkata"
# print(mydict)

#####Traversal in dictionary
# def traverse_dict(dict):
#     for i in dict:
#         print(i,dict[i])

# traverse_dict(mydict)

#######Search in dictionary
# def search_dict(dict, value):
#     for i in dict:
#         if dict[i] == value:
#             return i, value
#         else:
#             return "Not in the dictionary"

# print(search_dict(mydict,"Tirtho"))


#####Various methods of dictionary################



##Delete in dictionary

# mydict.pop('age')
# del mydict['age']
# mydict.clear()
# mydict_copy=mydict.copy()    ##Copy method
# print(mydict_copy)

# new_dict = {}.fromkeys(["a","b","c"],1)   ##Form Key


# print(mydict.get('age'))    ###Get Method

# print(mydict.items())

# print(mydict.popitem())

# print(mydict.setdefault('name1',"Tirtho_1"))     ##Set Default method
# print(mydict)  


##print(mydict.values())           ##Values


new_dict = {"a": 1, "b": 2, "c": 3}
mydict.update(new_dict)
print(mydict)
