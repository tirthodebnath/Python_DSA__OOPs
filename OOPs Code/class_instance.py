

class student:
    collage="ABC Collage"

    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    
    def display(self):
        print("Nmae is",self.name)
        print("Roll Number is",self.roll_no)
        print("Collage name is",self.collage)

std=student("123","Tirtho")
std.display()
std1=student("123","Archi")
std1.display()

