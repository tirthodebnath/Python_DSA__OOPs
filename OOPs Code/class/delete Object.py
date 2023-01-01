'''How to delete Object properties and Object in Python?
You can delete objects and properties of object by using the del keyword.'''

class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
 
 
emp1 = Employee(10000, "John Doe")

print(emp1.salary)
print(emp1.name)

del emp1.salary     # Delete object property
del emp1            # Delete object

'''after deleting the object, the object is not accessible anymore it wiil show given error
NameError: name 'emp1' is not defined'''

print(emp1.salary)
print(emp1.name)

