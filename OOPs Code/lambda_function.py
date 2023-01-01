def func(n):
    return lambda a : a * n
    func(5)
print(func(5)(2))