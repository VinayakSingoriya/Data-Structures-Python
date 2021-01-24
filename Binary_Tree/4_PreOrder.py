# Implementation of PreOrder Traversal of a Binary tree.
# Time Complexity : O(n)

# A class that represents an individual node in a binary tree.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function for traversal in PreOrder
def printPreorder(root):
    if root is not None:
        print(root.data, end=" ")
        printPreorder(root.left)   
        printPreorder(root.right)    

        
# Driver Mode
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(1)
    root.right = Node(6)        
    root.left.left = Node(5)
    root.left.right = Node(2)

    print("PreOrder is :", end = " ")
    printPreorder(root)  

