##How to update Object properties in Python?

class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
 
 
emp1 = Employee(10000, "John Doe")
print(emp1.salary)
 
emp1.salary = 20000   ## Updating the salary of emp1
print(emp1.salary)