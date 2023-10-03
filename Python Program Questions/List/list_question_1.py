##Input..........

# logs4 = [
#     ["1", "user_96", "resource_5"],
#     ["1", "user_10", "resource_5"],
#     ["301", "user_11", "resource_5"],
#     ["603", "user_12", "resource_5"],
#     ["301", "user_12", "resource_5"],  
#     ["1603", "user_12", "resource_7"],
# ]

# Output:
# {
#  'user_96': [1, 1],
#  'user_10': [1, 1],
#  'user_11': [301, 301],
#  'user_12': [301, 1603],
# }

logs4 = [
    ["1", "user_96", "resource_5"],
    ["1", "user_10", "resource_5"],
    ["301", "user_11", "resource_5"],
    ["603", "user_12", "resource_5"],
    ["301", "user_12", "resource_5"],
    ["1603", "user_12", "resource_7"],
]

output = {}

for row in logs4:
    if row[1] not in output:
        output[row[1]] = [int(row[0])]
        
        print(output)
    else:
        output[row[1]].append(int(row[0]))

for key, value in output.items():
    value.sort()
    output[key] = [value[0], value[-1]]

print(output)

