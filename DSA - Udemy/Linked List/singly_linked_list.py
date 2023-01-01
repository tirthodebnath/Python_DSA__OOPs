##Singly Linked List

##Creating a node with null values
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

#Creating the Head and Tail nodes, and assign None references to them
class Slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

singlylinkedlist = Slinkedlist()
node1= Node(1)
node2= Node(2)

singlylinkedlist.head=node1      ##Head
singlylinkedlist.head.next=node2  
singlylinkedlist.tail=node2      ##Tail


print(node1)