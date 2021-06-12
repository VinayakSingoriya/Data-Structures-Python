# Implementation of Inorder successor in a BST
# Time complexity : O(h), where h is the height of BST

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

def GetPredecessor(root, key):
    # Search the node
    current = search(root, key)
    if current is None:
        print("\n >> You have entered Invalid Key")
        exit()   
    if(current.left != None):
        # Case 1: Node has left subtree
        current = current.left
        # To find maximum (or) deepest rightmost node in left subtree
        while current.right != None:   
            current = current.right
        return  current
    else:
        # case 2: Node has no left subtree
        predecessor = None
        ancestor  = root
         # To find nearest ancestor for which given node would be in right subtree.
        while(ancestor != current):       
            if current.data > ancestor.data :
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left

        return predecessor

if __name__ == "__main__":
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
    pre= GetPredecessor(root, key)
    if pre:
        print(f"\nPredecessor of {key} :", pre.data)
    else:
        print(f'\nPredecessor of {key} : None')    


