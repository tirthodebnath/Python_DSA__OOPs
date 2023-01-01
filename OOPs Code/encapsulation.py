#private method in class

class car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print("driving")
    
    def __updatesoftware(self):
        print("Updating software")

car= car()

car.drive()

car.__updatesoftware()  ##This will provide error , because we can not access private method outside of class