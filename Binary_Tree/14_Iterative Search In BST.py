# Implementation of Searching Operation in a BST in a Iterative Way.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


# A utility function to search a given key in BST
def search(root, key):
 
    while(root != None):
        if key == root.data:
            return root

        elif key < root.data:
            root = root.left

        else:
            root = root.right

    return None            


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

print("Inorder Traversal of Tree is:")
printInorder(root)
key = 13
isFound = search(root, key)
if isFound:
    print(f"\n>> Element {key} Found\n")
else:
    print(f"\n>> Element {key} Not Found\n")
