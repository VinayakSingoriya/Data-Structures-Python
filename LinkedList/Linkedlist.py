class Node:

    #  Function to initialze Node
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # initialize next as null


# Linked list class contains a node object
class LinkedList:

    # Functions to initialize head of a linked list
    def __init__(self):
        self.head = None

    # Function to traverse a linked list
    def printData(self):           # O(n) time complexity
        print("Printing data: ")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Function to insert a new node at the beginning
    def push_atfront(self, data):            # O(1) time complexity
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node after a given nodes
    def insert_after(self, prev_node, new_data):    # O(1) time complexity
        if prev_node is None:
            print("The given node must be present in a linked list")
            return
        else:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    # Function to insert a new node at the end of a linked list
    def append(self, data):                 # O(n) time complexity
        new_node = Node(data)
        # If the Linked List is empty, then make the new node as head node
        if self.head is None:
            self.head = new_node
            return

        # else traverse till last node
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
        new_node.next = None

    # Delete the first occurence of a key in a linked list
    def delete_key(self, key):
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next

        # If key was not present in a linked list
        if (temp == None):
            return

         # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    # Delete at given Position

    def delete_position(self, pos):     # O(n) time complexity
        if self.head == None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = next

    # O(n) time complexity       # O(1) Space complexity
    def delete_list(self):
        current_node = self.head
        while current_node:
            temp = current_node.next
            del current_node.data
            current_node = temp

    # Iterative function to determine the length of a linked list
    def length_iterative(self):
        temp = self.head
        count = 0
        if temp is None:
            return 0
        while temp:
            temp = temp.next
            count += 1
        return count

     # This function counts number of nodes in Linked List
    # recursively, given 'node' as starting node.
    def getCountRec(self, node):
        if (not node):  # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    # A wrapper over getCountRec()
    def length_recursive(self):
        return self.getCountRec(self.head)


if __name__ == "__main__":
    l_list = LinkedList()  # Initialize linked list

    # Initialize nodes of a linked list

    l_list.head = Node(1)  # Initialized Head
    second = Node(2)
    third = Node(3)

    # Linking nodes
    l_list.head.next = second
    second.next = third

    # Traversing a linked list
    l_list.printData()

    # Inserting nodes and some performing basic operations
    l_list.push_atfront(23)
    print("linked list after insertion of 23 at the beginning: ")
    l_list.printData()
    l_list.insert_after(second, 44)
    print("linked list after insertion of 44 after second node: ")
    l_list.printData()
    l_list.append(12)
    print("linked list after insertion of 12 at the end:  ")
    l_list.printData()

    # Deletion of a node
    l_list.delete_key(44)
    print("Linked list after deletion of 44: ")
    l_list.printData()

    l_list.delete_position(2)
    print("Linked list after deletion of second node: ")
    l_list.printData()

    # Length of a linked list
    len = l_list.length_iterative()
    print(f"Lnegth of linked list(Iterative solution) is : {len}")

    len = l_list.length_recursive()
    print(f"Lnegth of linked list(recursive solution) is : {len}")

    # Deletion of a linked list
    print("Deleting Linked list...")
    l_list.delete_list()
    print("Linked list deleted")
