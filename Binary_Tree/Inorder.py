#Implementation of Inorder Traversal of a Binary Tree
# Time Complexity : O(n)

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data, end = " ")        
        printInorder(root.right)

# Driver mode
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(1)
    root.right = Node(6)        
    root.left.left = Node(5)
    root.left.right = Node(2)

    print("Inorder is :", end = " ")
    printInorder(root)         