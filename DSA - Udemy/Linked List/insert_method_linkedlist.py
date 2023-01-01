
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

    def __init__(self):
        node = self.head
        while node:
            yield node
            node = node.next

## Insert to Singly Linked List
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: 
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

##Traverse in singly linked list
def traverseSSL(self):
    if self.head is None:
        print("The singly linked list does not exist")
    else:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

##Search for a node in singly linked list
def searchSSL(self,nodeValue):
    if self.head is None:
        return "The list does not exist"
    else:
        node = self.head
        while node is not None:
            if node.value == nodeValue:
                return node.value
            node = node.next
        return "The value does not exist in the list"

##Delete a node from singly linked list
def deleteNode(self,location):
    if self.head is None:
        print("The list does not exist")
    else:
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head =self.head.next
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next=nextNode.next

##Delete entire SLL

def deleteEntireSSL(self):
    if self.head is None:
        print("The list does not exist")
    else:
        self.head = None
        self.tail = None




singlyLinkedList = Slinkedlist()
singlyLinkedList.insertSLL(1,1)
print([node.value for node in singlyLinkedList])