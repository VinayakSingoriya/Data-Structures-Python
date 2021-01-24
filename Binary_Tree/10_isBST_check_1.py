# Implemetation to check if the given tree is BST or not (Using Inorder Traversal).
# Note:- Inorder traversal of a BST give an sorted array/list in ascending order.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


prev = float('-inf')


def isBST(root):
    global prev
    # prev = None
    # return isBSTUtil(root, prev)
    if(root == None):
        return True
    if (isBST(root.left) == False):
        return False
    if (root.data <= prev):
        return False
    prev = root.data
    return isBST(root.right)


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
    if isBST(root):
        print("Is BST")
    else:
        print("Not a BST")
