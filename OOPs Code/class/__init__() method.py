'''How to use the __init__() method to assign values to data attributes in Python?
Python classes have a special method named __init__ which is automatically executed 
when an instance of the class is created in memory.'''


class Employee:
        def __init__(self, salary, name):
                self.salary = salary
                self.name = name
 
 
emp1 = Employee(10000, "John Doe")
print(emp1.salary)
print(emp1.name)