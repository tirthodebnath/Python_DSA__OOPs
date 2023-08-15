names = ["kalyan", "Krish", "Ashu", "Abdul"]
marks = [29, 71, 95, 32]
passing = 35

result_dict = {}

dict=dict(zip(names,marks))
print(dict)

for name, mark in zip(names, marks):
    if mark >= passing:
        result_dict[name] = "Pass"
    else:
        result_dict[name] = "Fail"

print(result_dict)


