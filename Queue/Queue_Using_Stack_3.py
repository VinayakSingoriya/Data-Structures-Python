# Implementation of Queue using one stack and recursive call stack (IMPORTANT)
class Queue:
    def __init__(self):
        self.s = []

    def enQueue(self, x):
        self.s.append(x)    

    def deQueue(self):
        # condition for empty Queue
        if(len(self.s)<=0):   
            print("Queue is Empty")
            return 

        # Pop an item from the stack
        x = self.s[len(self.s)-1]
        self.s.pop()

        # If stack becomes empty the return the popped item   
        if len(self.s)<=0:
            return x    

        # Recursive call
        item = self.deQueue()
        print(item)

        # Push poppes item back to the stack
        self.s.append(x)
        # print(self.s)

        #Return the result of the dequeue() call
        return item

if __name__ == "__main__":
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    q.enQueue(4)

    print(q.deQueue())
    