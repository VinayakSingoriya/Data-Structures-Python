# Iterative implementation of insertion in a BST
# Time complexity : O(h), where h is the height of BST

class Node:
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data, end = " ")        
        printInorder(root.right)

def insert(root, key):
    prev = None
    while (root != None):
        prev  = root
        if (key == root.data):
            return
        elif (key < root.data):
            root  = root.left
        else:
            root  = root.right

    if key < prev.data:
        prev.left = Node(key)
    else:
        prev.right = Node(key)                                
            

           

if __name__ == "__main__":
            
    r = Node(8)
    insert(r, 3)
    insert(r, 1)
    insert(r, 6)
    insert(r, 10)
    insert(r, 14)
    insert(r, 13)
    insert(r, 4)
    insert(r, 7)
    insert(r, 9)
    insert(r,2)
    insert(r, 2)
    insert(r, 4)
    printInorder(r)
