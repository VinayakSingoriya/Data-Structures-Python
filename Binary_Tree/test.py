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

isBST([1,2,3,4])