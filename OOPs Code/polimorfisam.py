#Polimorfisom

class dog:
    def sound(self):
        print("Bow Bow")

class cat:
    def sound(self):
        print("Mew Mew")

def make_sound(animal_type):
    animal_type.sound()

f1=dog()
f2=cat()

make_sound(f1)
make_sound(f2)