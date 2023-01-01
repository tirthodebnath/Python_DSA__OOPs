#Multiple inharitance

class land_animal:
    def func1(self):
        print("This is the first class")

class water_animal:
    def func2(self):
        print("This is the second class")

class frog(land_animal,water_animal):
    pass

f=frog()
f.func1()
f.func2()               