#Method over riding

class a:
    def display(self):                           
        print("This methid belongs to class a")

class b:
    def display(self):                                              #deriving the same method from class a
        print("This method belongs to class b")   

p=b()
p.display()
