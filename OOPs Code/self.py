## self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. 
#It binds the attributes with the given arguments. 
from matplotlib.pyplot import cla


class person:
    def display(self):
        print("Hello World")

p=person()
p.display()

