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

#creating method for search operation
    def search(self,data):
        if self.key ==data:
            print("Node is found")
            return
        if self.key > data:
            if self.left_child:
                self.left_child.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.right_child:
                self.right_child.search(data)
            else:
                print("Node is not present in tree!")

#creating methods for pre-order traversal
    def pre_order(self):
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

#creating methods for in-order traversal
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.key)    
        if self.right_child:
            self.right_child.in_order() 

#creating methods for in-order traversal
    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()    
        print(self.key)    

#creating the delete method
    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.right_child:
                self.left_child = self.left_child.delete(data)   
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.right_child:
                self.right_child = self.right_child.delete(data)    
            else:
                print("Given node is not present in the tree") 
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            if self.right_child is None:
                temp = self.left_child
                self=None
                return temp
            node= self.right_child
            while node.left_child:
                node = node.left_child  
            self.key = node.key
            self.right_child = self.right_child.delete(node.key)    
        return self               
                    

#creating object from class BinarySearchTree        
root=BinarySearchTree(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
#print("Pre-order traversal")    
#root.pre_order()
#print("In-order traversal")
#root.in_order()
#print("Post-order traversal")
#root.post_order()
root.delete()
root.pre_order()