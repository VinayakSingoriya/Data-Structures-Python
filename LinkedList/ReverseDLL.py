
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

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev


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

    print("Reverse DLL :")
    lList.reverse()
    lList.printList(lList.head)