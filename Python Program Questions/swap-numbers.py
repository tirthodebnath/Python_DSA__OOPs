#Swap Two Variables

#Using a temporary variable
x = 5
y = 10

temp = x     # create a temporary variable and swap the values
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#Without Using Temporary Variable
def swap(a,b):
    a,b = b,a
    return a,b
print(swap(5,10))

