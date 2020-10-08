class Node:
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CirculaLinkedList:
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a  circular linked list
    def push(self, data):
        newNode = Node(data)  # Creating a new node
        temp = self.head

        newNode.next = self.head

        # If linked list is not None then set the next of last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newNode

        else:
            newNode.next = newNode    # For the first node

        self.head = newNode

    def splitList(self, head1, head2):            # O(n) time complexity
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is None:
            return

        # If htere are odd nodes in the circular list then
        # fast_ptr->next becomes head and for even nodes
        # fast_ptr->next->next becomes head
        while(fast_ptr.next != self.head and fast_ptr.next.next != self.head):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # If there are even elements in list then
        # move fast_ptr
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next

         # Set the head pointer of first half
        head1.head = self.head

        # Set the head pointer of second half
        if self.head.next != self.head:
            head2.head = slow_ptr.next

        # Make second half Circular
        fast_ptr.next = slow_ptr.next
        # Make first half circular
        slow_ptr.next = self.head

    def printList(self):           # O(n) time complexity
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


if __name__ == "__main__":
    cList = CirculaLinkedList()
    head1 = CirculaLinkedList()
    head2 = CirculaLinkedList()
    cList.push(2)
    cList.push(3)
    cList.push(4)
    cList.push(5)
    cList.push(6)
    cList.push(23)

    print("Original Circular Linked list is :")
    cList.printList()

    # Split the list
    cList.splitList(head1, head2)

    print("First half circular Linked list:")
    head1.printList()
    print("Second half circular Linked List:")
    head2.printList()
