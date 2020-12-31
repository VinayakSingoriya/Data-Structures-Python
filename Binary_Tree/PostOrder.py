# Implementation of Postorder traversal of a given binary Tree.
# Time Complexity : O(n)

# A class that represents an individual Node in Binary Tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# A function for traversal in Postorder
def printPostorder(root):
    if root is not None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end = " ")

# Driver mode
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(1)
    root.right = Node(6)        
    root.left.left = Node(5)
    root.left.right = Node(2)

    print("PostOrder is :", end = " ")
    printPostorder(root) 
