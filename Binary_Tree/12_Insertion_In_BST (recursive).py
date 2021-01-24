# Recursive implementation of insertion in a BST
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
    if root is None: 
        return Node(key) 
    else: 
        if root.data == key: 
            return root 
        elif root.data < key: 
            root.right = insert(root.right, key) 
        else: 
            root.left = insert(root.left, key) 
    return root        
            

           

if __name__ == "__main__":
            
    r = Node(8)
    insert(r, 3)
    # insert(r, 1)
    # insert(r, 6)
    # insert(r, 10)
    # insert(r, 14)
    # insert(r, 13)
    # insert(r, 4)
    # insert(r, 7)
    # insert(r, 9)
    printInorder(r)
