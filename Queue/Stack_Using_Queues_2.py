# Implementation of Stack using Queues by making Pop() operation costlier...

from queue import Queue
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0
    

    def push(self, x):
        # Append new element to q1
        self.q1.put(x)
        self.curr_size+=1 
  
    def pop(self):
        if self.q1.empty():
            print("Stack is empty")
            return

        self.a_size = self.curr_size    


        while self.a_size!=1:
            self.a_size-=1
            self.q2.put(self.q1.queue[0])
            self.q1.get()  
        self.q1.get()  
        self.curr_size-=1  

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def top(self):
        return self.q1.queue[self.curr_size-1]


if __name__ == "__main__":
    s = Stack()            
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    print("size: ", s.curr_size)
    print("top: ", s.top())
    s.pop()
    print("After POP:")
    print("size: ", s.curr_size)
    print("top: ", s.top())



