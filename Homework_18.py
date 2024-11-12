########################################
#Homework_18 Task_1
########################################
# Define a Node class to represent each node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Define the BinaryTree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Helper function to insert nodes in a binary tree
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    # Function to print all leaf nodes
    def printLeafNodes(self, node):
        if node:
            # A leaf node has no children
            if not node.left and not node.right:
                print(node.data, end=' ')
            else:
                self.printLeafNodes(node.left)
                self.printLeafNodes(node.right)

    # Function to count the number of edges in the tree
    def countEdges(self, node):
        # An empty tree has no edges
        if not node:
            return 0
        # Recursively count edges in left and right subtrees and add 1 for the edge to the child node
        left_edges = self.countEdges(node.left)
        right_edges = self.countEdges(node.right)
        return left_edges + right_edges + (1 if node.left or node.right else 0)

# Example usage:
tree = BinaryTree()
# Insert nodes into the tree
nodes = [10, 5, 20, 3, 7, 15, 30]
for n in nodes:
    tree.insert(n)

print("Leaf nodes in the binary tree:")
tree.printLeafNodes(tree.root)  # Output: All leaf nodes in the tree

print("\nTotal number of edges in the binary tree:")
edges = tree.countEdges(tree.root)
print(edges)  # Output: Total number of edges

############################################
