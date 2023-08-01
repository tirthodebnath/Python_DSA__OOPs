class BinarySearchTree:
    def __init__(self,key):
        self.key=key
        self.left_child=None
        self.right_child=None

#defining the method for insertion operation
    def insert(self,data):
        if self.key is None:     #checking tree is empty or not
            self.key=data
            return
        if self.key==data:
            return    
        if self.key > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child=BinarySearchTree(data)
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child=BinarySearchTree(data)        

                    
#creating object from class BinarySearchTree        
root=BinarySearchTree(10)
list1 = [10,1,3,4,2]
for i in list1:
    root.insert(i)

