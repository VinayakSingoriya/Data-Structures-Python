# Implemention of stack using Two Queues by making Push operation costlier

from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        # Push x first in the empty q2
        self.q2.put(x)

        # Push all the remaining elements from q1 to q2
        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        # Swap the names of Queues
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):
        if self.q1.empty():
            print("Stack is empty")
            return

        self.q1.get()
        self.curr_size -= 1

    def top(self):
        if self.q1.empty():
            print("Stack is empty")
            return
        return self.q1.queue[0]

    def size(self):
        return self.curr_size

if __name__ == "__main__":
    s  = Stack()

    s.push(1)                    
    s.push(2)                    
    s.push(3)                    
    s.push(4)  
    print("Size: ", s.size())
    print("top:",s.top())                  
    s.pop()
    print(s.top())
    print("size: ", s.size())
