# Implementation of Queue Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue
# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:
    def __init__(self):  # Initialize queue by set front and rear to None
        self.front = self.rear = None

    def isEmpty(self):  # Condition of empty Queue
        return self.front == None

    def enqueue(self, item):  # Adds an item in a queue
        temp = Node(item)

        if (self.rear == None):  # If Queue is Empty
            self.rear = self.front = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):  # Removes an item from the Queue
        if self.isEmpty():
            print("Queue is Empty")
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None


if __name__ == "__main__":
    Q = Queue()
    empty = Q.isEmpty()
    print(empty)
    Q.enqueue(25)
    Q.enqueue(26)
    Q.enqueue(27)
    Q.enqueue(28)
    Q.enqueue(29)
    print("Intitially \n Queue front : " + str(Q.front.data))
    print("Queue rear :" + str(Q.rear.data))
    Q.dequeue()
    Q.dequeue()
    print("After Two dequeue:")
    print("Queue front: " + str(Q.front.data))
    print("Queue rear: " + str(Q.rear.data))
