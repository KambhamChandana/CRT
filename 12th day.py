class Node:
    def _init_(self):
        self.left = None
        self.right = None
        self.data = None
    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data)
            self.inorder_traversal(Node.right)
    def sum_of_nodes(self,Node):
        if Node is None:
            return 0
        return Node.data + self.sum_of_nodes(Node.left) + self.sum_of_nodes(Node.right)
    def count_nodes(self,Node):
        if (Node is None):
            return 0
        return 1+self.count_nodes(Node.left) + self.count_nodes(Node.right)

        

tree= Node()
tree.data = 1 
tree.left = Node()
tree.left.data = 2
tree.right = Node()
tree.right.data = 3
tree.left.left = Node()
tree.left.left.data = 4
tree.left.right = Node()
tree.left.right.data = 5
tree.right.left=Node()  
tree.right.left.data = 6
tree.right.right = Node()
tree.right.right.data = 7
tree.inorder_traversal(Node=tree)
print(tree.sum_of_nodes(Node=tree)) 
print(tree.sum_of_nodes(Node=tree.left))
print(tree.sum_of_nodes(Node=tree.right))
print(tree.count_nodes(Node=tree.right))
print(tree.count_nodes(Node=tree.left))
print(tree.count_nodes(Node=tree))

