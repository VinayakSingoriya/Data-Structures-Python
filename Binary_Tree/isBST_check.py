class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printInorder(root):
    if root is not None:
        printInorder(root.left)
        result.append(root.data)
        print(root.data, end = " ")             
        printInorder(root.right)
    return result            

def isBST(result):
    for i in range(0, len(result)):
        for j in range(i+1, len(result)):
            if result[i] >=result[j]:
                print("\nGiven Binary Tree is NOT BST.")
                print(i,j)
                return
            else:
                continue

    print("\nGiven Binary Tree is a BST.")        
                


root = Node(8)
root.left = Node(3)
root.right = Node(10)         
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left =Node(13)

result  = list()

print("Inorder Traversal of Tree is:")
result = printInorder(root)
isBST(result)

