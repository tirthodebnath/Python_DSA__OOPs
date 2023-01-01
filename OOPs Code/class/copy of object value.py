'''How to copy all properties of an object to another object in Python?'''

class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()
        self.foo = 1
        self.bar = 2
 
 
obj1 = MyClass()
obj2 = MyClass()
 
obj1.foo = 25
obj2.__dict__.update(obj1.__dict__)
 
print(obj1.foo)
print(obj2.foo)