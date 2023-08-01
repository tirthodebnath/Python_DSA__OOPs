a = ["kalyan", "Krish", "Ashu", "Abdul"]
marks = [29, 71, 95, 32]
passing = 35

##From the above data give the below putput
{'kalyan': 'Fail', 'Krish': 'Pass', 'Ashu': 'Pass', 'Abdul': 'Fail'}


result_dict = {}

for name, mark in zip(a,marks):
    if mark > 35:
        result_dict[name]="Pass"
    else:
        result_dict[name]="Fail"

print(result_dict)