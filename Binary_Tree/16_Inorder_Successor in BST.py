# Implementation of Searching Operation in a BST.
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

def search(root, key):

    # Base Cases: root is null or key is present at root
    if root is None or root.data == key:
        return root

    # Key is greater than root's key
    if root.data < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

def GetSuccessor(root, key):
    # Search the node
    current = search(root, key)
    if current is None:
        return None   
    if(current.right != None):
        # Case 1: Node has right subtree
        current = current.right
        # To find minimum (or) deepest leftmost node in right subtree
        while current.left != None:   
            current = current.left
        return  current
    else:
        # case 2: Node has no right subtree
        successor = None
        ancestor  = root
         # To find nearest ancestor for which given node would be in left subtree.
        while(ancestor != current):       
            if current.data < ancestor.data :
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return successor

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
key =  25
succ = GetSuccessor(root, key)
if succ:
    print(f"\nSuccessor of {key} :", succ.data)
else:
    print(f'\nSuccessor of {key} : None')    


