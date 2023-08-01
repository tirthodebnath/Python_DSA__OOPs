#Delete from beggining of the linkedlist
def delete_begin(self):
    if self.head is None:
        print("Linked list is empty")
    else:
        self.head=self.head.ref


#Delete from end of the linkedlist
def delete_end(self):
    if self.head is None:
        print("Linked list is empty so we can't delete the node")
    elif self.head.ref is None:
        self.head = None    
    else:
        n=self.head
        while n.ref.ref is None:
            n = n.ref 
        n.ref=None

#Delete by value from linkedlist
def delete_by_value(self,x):
    if self.head is None:
        print("Linked list empty")
        return
    if x==self.head.data:
        self.head=self.head.ref
        return
    n = self.head
    while n.ref is not None:
        if x==n.ref.data:
            break
        n=n.ref
    if n.ref is None:
        print("Node is not present")
    else:
        n.ref=n.ref.ref            
            







