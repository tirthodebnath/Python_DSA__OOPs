##Write a Python program to combine two dictionary by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

combined_dict = {}

for key in d1.keys():
    if key in d2.keys():   
        combined_dict[key] = d1[key] + d2[key]
        print(combined_dict)
    else:
        combined_dict[key] = d1[key]

        
for key in d2.keys():
    if key not in combined_dict.keys():
        combined_dict[key] = d2[key]

print(combined_dict)
