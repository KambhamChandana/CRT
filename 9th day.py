class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
class bst:
    def __init__(self):
        self.root=None()
    def insert(self,data,root):
    if (root<root.data):
        return Node(data)
        # if data<root--->left rcc call
        if(data<root.data):
            root.left=self.insert(data,root.left)
        elif(data>root.data):
            root.right=self.insert(dta,root.right)
        return root
def inorder_traversal(self,root):
     if(root is None):
          self.inorder_traversal(root.left)
          print(root.dta,end=" ")
          self.inorder_traversal(root.right)
def preorder_traversal(self,root):
     pass
def postorder_traversal(self,root):
     pass
bst_tree=bst
root=Node()
bst_tree.insert(20,root)
bst_tree.insert(10,root) 
bst_tree.insert(900,root)

