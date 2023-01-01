#Inheriting the class animal to call dog
class animal:
    def eating(self):
        print("Dog")        


class dog(animal):
    def display(self):
        print("Huskey")

d=dog()
d.eating()
d.display()      