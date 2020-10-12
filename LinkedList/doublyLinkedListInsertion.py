

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):  # Insert a node at the beginning of a DLL
        new_node = Node(data)

        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, data):  # Insert a new node after a given node in a DLL
        if prev_node is None:
            print("The given previous node cannot be null/None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, data):       # Insert a new node at the end of a DLL
        new_node = Node(data)
        new_node.next = None
        last = self.head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Insert a new node before a given node in a DLL
    def insertBefore(self, next_node, data):
        if next_node is None:
            print("Any new node cannot be added before a null/None")
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            new_node = self.head

    def deleteNode(self, dele):

        # Base Case
        if self.head is None and dele is None:
            return

        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is not the last Node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # change prev only if the node to be deleted is not the head node
        if dele.prev is not None:
            dele.prev.next = dele.next

        # Finally free the memory occupied by dele
        # call the python garbage collector
        gc.collect()

    def printList(self, node):
        print("-----------------------------------------")
        print("Traversal in forward direction in DLL : ")
        while(node is not None):
            print(node.data, end=" ")
            last = node
            node = node.next

        print("\nTraversal in a backward direction in DLL :")
        while(last is not None):
            print(last.data, end=" ")
            last = last.prev
        print("\n-----------------------------------------")


if __name__ == "__main__":
    lList = LinkedList()
    lList.append(3)
    lList.append(4)
    lList.append(5)
    lList.append(6)
    lList.append(7)
    lList.append(8)
    print("Creating Doubly Linked List :")
    lList.printList(lList.head)

    lList.push(2)
    print(" DLL after inserting 2 at the beginning :")
    lList.printList(lList.head)

    lList.append(10)
    print(" DLL after inserting 10 at the end :")
    lList.printList(lList.head)

    lList.insertAfter(lList.head.next, 11)
    print(" DLL after inserting 11 after second node :")
    lList.printList(lList.head)

    lList.insertBefore(lList.head.next, 12)
    print(" DLL after inserting 12 before second node :")
    lList.printList(lList.head)

    lList.deleteNode(lList.head)
    print("DLL after deletion of head node :")
    lList.printList(lList.head)

    lList.deleteNode(lList.head)
    print("DLL after deletion of head node :")
    lList.printList(lList.head)

    lList.deleteNode(lList.head)
    print("DLL after deletion of head node :")
    lList.printList(lList.head)
