# Imlplementation of Circular Queue through array(python list)

class CircularQueue():
    def __init__(self, size):
        self.size = size
        self.Q = [None]*size
        self.front = self.rear = -1

    def enqueue(self, data):  # Time Complexity : O(1)
        # condition if queue is full
        if((self.rear + 1) % self.size == self.front):
            print("Queue if OVERFLOW")

        # condition for empty queue
        elif(self.front == -1):
            self.front = self. rear = 0
            self.Q[self.rear] = data
        else:
            #  set element at next position of rear
            self.rear = (self.rear+1) % self.size
            self.Q[self.rear] = data

    def dequeue(self):  # Time Complexity : O(1)
        # condition for empty queue
        if (self.front == -1):
            print("Queue is UNDERFLOW")

        # Conditio for only one element
        if (self.rear == self.front):
            temp = self.Q[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.Q[self.front]
            self.front = (self.front+1) % self.size
            return temp

    def display(self):
        # Condition for empty queue
        if (self.front == -1):
            print("Queue is UNDERFLOW")
        elif(self.rear >= self.front):
            print("Elements in the circular queue are: ", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.Q[i], end=" ")
            print()

        else:
            print("Elements int the Circular Queue are: ", end=" ")
            for i in range(self.front, self.size):
                print(self.Q[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.Q[i], end=" ")

            print()

        if ((self.rear+1) % self.size == self.front):
            print("Queue is OVERFLOW")


if __name__ == '__main__':
    Q = CircularQueue(10)
    Q.enqueue(23)
    Q.enqueue(24)
    Q.enqueue(25)
    Q.enqueue(26)
    Q.display()
    print("deleted value: ", Q.dequeue())
    Q.display()
    print("deleted value: ", Q.dequeue())
    Q.display()
