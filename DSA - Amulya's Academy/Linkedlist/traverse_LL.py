#Travaerse the linked list
class Node:                    #class Node
    def __init__(self,data):
        self.data=data
        self.ref=None

node1=Node(10)
print(node1) 

class LinkedList:             #LinkedList class
    def __init__(self):
        self.head=None

    def print__LL(self):          #traversal operation
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n= n.ref 

LL1=LinkedList()
LL1.print__LL()                       