## Stack push,pop,peek,delete
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    #isEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    #Push
    def push(self,value):
        self.list.append(value) 
        return "Item is added to stack"

    #pop
    def pop(self):
        if self.isEmpty():
            return "There no element in the stack"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "There no element in the stack"
        else:
            return self.list[len(self.list)-1]

    #delete
    def delete(self):
        self.list=None                    


classStack = Stack()
classStack.push(10)
classStack.push(11)
classStack.push(12)
classStack.push(13)
print(classStack.delete())
