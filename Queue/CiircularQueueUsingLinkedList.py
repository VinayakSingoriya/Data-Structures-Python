# Implementation of Circular Queue Using Circular Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue():

    def __init__(self):
        self.rear = self.front = None

    def isEmpty(self):  # Condition for empty queue
        return self.front == None

    def enqueue(self, data):  # Adds an item in a queue
        newNode = Node(data)

        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.rear.next = self.front

    def dequeue(self):  # Removes an item from the queue
        if self.isEmpty():
            print("Queue is Empty")
            return
        value = None
        if self.front == self.rear:  # If there is only one node in a queue
            value = self.front.data
            self.front = self.rear = None
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.next
            self.rear.next = self.front


if __name__ == "__main__":
    Q = CircularQueue()
    temp = Q.isEmpty()
    print("Empty :", temp)
    Q.enqueue(23)
    Q.enqueue(24)
    Q.enqueue(25)
    Q.enqueue(26)
    Q.enqueue(27)
    print("Initially :")
    print("Queue front : ", Q.front.data)
    print("Queue rear :", Q.rear.data)
    Q.dequeue()
    Q.dequeue()
    print("After 2 Dequeued:")
    print("Queue front :", Q.front.data)
    print("Queue rear :", Q.rear.data)
