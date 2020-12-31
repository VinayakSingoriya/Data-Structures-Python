# Implementation of a Inorder traversal without using recursion(With the help of stack)

'''
ALGORITHM:
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
'''

class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# Iterative function for inorder tree traversal 
def inOrder(root): 
      
    # Set current to root of binary tree 
    current = root  
    stack = [] # initialize stack 
    done = 0 
      
    while True: 
          
        # Reach the left most Node of the current Node 
        if current is not None: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            stack.append(current) 
          
            current = current.left  
  
          
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        elif(stack): 
            current = stack.pop() 
            print(current.data, end=" ") # Python 3 printing 
          
            # We have visited the node and its left  
            # subtree. Now, it's right subtree's turn 
            current = current.right  
  
        else: 
            break
       
    print() 
  
  
""" Constructed binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print('Inorder is :', end=" ")
inOrder(root) 