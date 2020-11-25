# Stack implementation using a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of Stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    # Get the current sze of the Stack
    def getSize(self):
        return self.size

    # Chexk if the stack is empty or not
    def isEmpty(self):
        return self.size == 0

    # Get a top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking form an empty stack")
        return self.head.next.value

    # Push a value into the Stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size -= 1

    # Remove the value from the stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Poping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    for i in range(1, 6):
        remove = stack.pop()
        print(f"Pop : {remove}")
    print(f"Stack: {stack}")
