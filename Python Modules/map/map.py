def evn_odd(num):
    if num % 2==0:
        return "Even"
    else:
        return "Odd"

lst=[1,2,3,4,5,6,7,8,9]

print(list(map(evn_odd,lst)))
    