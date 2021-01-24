
# Implementation of a Insertion of a new node in a tree via Level-Order Traversal

class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
 
# function to insert element in binary tree
def insert(temp,key):
 
    if not temp:
        root = newNode(key)
        return
    q = [] 
    q.append(temp) 
 
    # Do level order traversal until we find 
    # an empty place. 
    while (len(q)): 
        temp = q[0] 
        q.pop(0) 
 
        if (not temp.left):
            temp.left = Node(key) 
            break
        else:
            q.append(temp.left) 
 
        if (not temp.right):
            temp.right = Node(key) 
            break
        else:
            q.append(temp.right)

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data, end = " ")        
        printInorder(root.right)             

               
 
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal of a Tree: ", end=" ")
printInorder(root)
insert(root, 7)
print("\nAfter Insetion InOrder will be: ", end = " ")
printInorder(root)