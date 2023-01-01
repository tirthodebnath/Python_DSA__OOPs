'''How to create and call Method of a Class in Python?
Methods in classes are functions that belong to the class.'''

class Employee:
    salary = 10000
    name = "John Doe"
 
    def tax(self,var1,var2):
        self.var1 = var1 
        self.var2 = var2
        print(self.salary * 0.10)
        print(self.var1)
        print(self.var2)
        
 
 
emp1 = Employee()
print(emp1.salary)
print(emp1.name)
emp1.tax(100,"tirtho")