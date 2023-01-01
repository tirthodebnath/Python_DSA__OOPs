##Print all properties of an Object in Python
class Animal(object):
    def __init__(self):
        self.eyes = 2
        self.name = 'Dog'
        self.color= 'Spotted'
        self.legs= 4
        self.age  = 10
        self.kids = 0
 
 
animal = Animal()
animal.tail = 1
 
temp = vars(animal)
for item in temp:
    print(item, ':', temp[item])