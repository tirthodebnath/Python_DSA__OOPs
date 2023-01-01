a=5
b=0

try:
    print(a/b)

except Exception as e:
    print("We can not devide a number by 0", e)

finally:
    print("Finally printing")
