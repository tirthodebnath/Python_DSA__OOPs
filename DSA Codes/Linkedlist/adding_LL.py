#Adding to the linked list
class Node:                       #class Node
    def __init__(self,data):
        self.data=data
        self.ref=None

node1=Node(10)
print(node1) 

class LinkedList:                 #LinkedList class
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

#Add begining of the linked list
    def add_begin(self, data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

#Add at the end of the linked list
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:   
            n= self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node  

#Add after a node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
        n=n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            new_ref=new_node

#Add before a node
    def add_before(self,data,x):
        if self.data is None:
            print("Linked list is empty")
            return
            if self.head.data==x:
                new_node=Node(data)
                new_node.ref=self.head
            self.head=new_node
            return
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n= n.ref
                if n.ref is None:
                    print("Node is not found")
                else:
                    new_node=Node(data)
                    new_node.ref=n.ref
                    n.ref=new_node            

LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(100)
LL1.add_after(20)
LL1.add_before(30,100)
LL1.add_end(100)
LL1.print__LL()        
