## Multi level inheritance
class name:
    def func1(self):
        print("My name is Tirthankar")

class age(name):
    def func2(self):
        print("Mu age is 24")

class sex(age):
    def func3(self):
        print("I am a male")

p=sex()
p.func1()
p.func2()
p.func3()        
