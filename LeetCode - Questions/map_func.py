#Define map function....

#eg 1:
def mufunc(a,b):
      return a+b

x = map(mufunc,(2,3),(4,5))
print(list(x))

#eg 2:
def mufunc(a,b):
      return a+b

x = map(mufunc,("Tirtho","West"),("Debnath","Bengal"))
print(list(x))