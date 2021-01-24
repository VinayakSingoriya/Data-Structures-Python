# To check if the given tree is BST or not (by specifying range of each node between min and max)
# Time Complexity: O(n)
# Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)

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


def isBST(node, minKey, maxKey):

    # base case
    if node is None:
        return True

    # if node's value fall outside valid range
    if node.data < minKey or node.data > maxKey:
        return False

    # recursively check left and right subtrees with updated range
    return isBST(node.left, minKey, node.data) and \
        isBST(node.right, node.data, maxKey)


# Function to determine if given Binary Tree is a BST or not
def checkForBST(root):

    if isBST(root, float('-inf'), float('inf')):
        print("\nThis is a BST.")
    else:
        print("\nThis is NOT a BST")


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
checkForBST(root)
