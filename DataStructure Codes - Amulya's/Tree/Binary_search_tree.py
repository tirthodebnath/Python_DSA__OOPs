class BinarySearchTree:
    def __init__(self,key):
        self.key=key
        self.left_child=None
        self.right_child=None

#creating object from class BinarySearchTree        
root=BinarySearchTree(10)
print(root.key)
print(root.left_child)
print(root.right_child)         

#creating the left child
root.left_child=BinarySearchTree(5)
print(root.key)
print(root.left_child)
print(root.right_child)
print(root.left_child.key)
print(root.left_child.left_child)
print(root.left_child.right_child)


