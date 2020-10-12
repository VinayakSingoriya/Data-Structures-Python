import gc  # Gabage collector module


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

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
    lList.append(2)
    lList.append(3)
    lList.append(4)
    lList.append(5)
    lList.append(6)
    lList.append(7)
    lList.append(8)

    print("Original DLL :")
    lList.printList(lList.head)

    lList.deleteNode(lList.head)
    print("DLL after deletion of first node :")
    lList.printList(lList.head)

    lList.deleteNode(lList.head.next)
    print("DLL after deletion of second node :")
    lList.printList(lList.head)
