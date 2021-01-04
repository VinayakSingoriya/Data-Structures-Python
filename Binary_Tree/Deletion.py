# Program to implement deletion in  a Binary Tree

# class to create a node with data, left child and right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to delete the given deepest node(del_node) in binary tree(via level-order Traversal)
def deleteDeepest(root, del_node):
    q = []
    q.append(root)
    while(len(q)>0):
        temp = q.pop(0)
        if temp is del_node:
            temp  = None
            return
        if temp.left:
            if temp.left is del_node:
                temp.left = None
                return
            else:
                q.append(temp.left) 

        if temp.right:
            if temp.right is del_node:
                temp.right = None
                return
            else:
                q.append(temp.right)        


# Function to delete element in Binary tree(Via level-order Traversal)
def deleteNode(root, key):
    if root == None:
        return None

    if root.left == None and root.right == None:
        if root.data == key:
            return None
        else:
            return root


    target_node = None
    queue = []                
    queue.append(root)
    while(len(queue)>0):
        temp = queue.pop(0)
        
        if temp.data == key:
            target_node = temp
        if temp.left is not None:
            queue.append(temp.left)    
        if temp.right is not None:
            queue.append(temp.right)

    if target_node:
        x = temp.data  #Data of bottomost and rightmost node(i.e. last node)
        deleteDeepest(root, temp)
        target_node.data  = x      

    return root



# Function to Print Inorder of a Binary Tree
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data, end = " ")        
        printInorder(root.right)        

# Drivers mode
if __name__=='__main__': 
    root = Node(10) 
    root.left = Node(11) 
    root.left.left = Node(7) 
    root.left.right = Node(12) 
    root.right = Node(9) 
    root.right.left = Node(15) 
    root.right.right = Node(8) 

    print("The inorder traversal of tree before deletion: ", end =" ")
    printInorder(root)

    key = 11
    root = deleteNode(root, key)
    print("\nThe Inorder traversal after Deletion: ", end = " ")
    printInorder(root)
    