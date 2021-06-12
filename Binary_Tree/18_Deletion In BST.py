# Implementation of a delete a node in a BST

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

def GetSuccessor(root, node):
    # Search the node
    current = node  
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


def deleteNode(root, key):
    current = search(root, key)
    print()
    print(current.data)
    if current == None:
        print("Key Not Found")
        exit()
    # Case 1: No child
    if (current.right==None and current.left==None):
        current = None
    # Case 2: one child
    elif (current.left == None):
        temp = current
        current = current.right
        temp = None
    elif (current.right == None):
        temp =  current
        current = current.left
        temp = None
    # Case 3: Two children
    else:
        temp = GetSuccessor(root, current)
        current.data = temp.data
        current.right = deleteNode(current.right, temp.data)
    return current
    
if __name__ == '__main__':
    root = Node(8);
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    print("Inorder is :", end = " ")
    printInorder(root) 

    deleteNode(root,3) 
    print("\n After delete:")
    print("Inorder is :", end = " ")
    printInorder(root)     
    
     
       
