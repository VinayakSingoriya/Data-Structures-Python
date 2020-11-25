class Queue:

    def __init__(self, capacity):  # Initialization of Queue
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):  # Function to check if queue is full or not
        return self.size == self.capacity

    def isEmpty(self):  # Check whether queue is empty or not
        return self.size == 0

    def enqueue(self, item):  # Adds an item to the queue and change rear and size
        if self.isFull():
            print("Queue is OVERFLOW")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print(f"{item} is enqueued to the queue")

    def dequeue(self):  # removes an item from the queue and change front and size
        if self.isEmpty():
            print("Queue is UNDERFLOW")
            return
        print(f"{self.Q[self.front]} is dequeued from the queue")
        self.front = (self.front+1) % self.capacity
        self.size = self.size - 1

    def que_front(self):  # Function to get front element
        if self.isEmpty():
            print("Queue is UNDERFLOW")
            return
        print("Front elememt is: ", self.Q[self.front])

    def que_rear(self):  # Function to get rear element
        if self.isEmpty():
            print("Queue is UNDERFLOW")
            return
        print("Rear element is :", self.Q[self.rear])


if __name__ == "__main__":
    queue = Queue(10)
    queue.enqueue(25)
    queue.enqueue(26)
    queue.enqueue(27)
    queue.enqueue(28)
    queue.enqueue(29)
    queue.enqueue(30)
    queue.enqueue(31)
    queue.enqueue(32)
    queue.enqueue(33)
    queue.enqueue(34)
    queue.enqueue(34)
    queue.que_front()
    queue.que_rear()
    queue.dequeue()
    queue.que_front()
    queue.que_rear()
