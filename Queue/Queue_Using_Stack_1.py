# Implement Queue using stack by using two stacks with costly enQueue()
class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):       #Time complexity : O(n), Auxiliary space: O(n)
        # Move all the elements from S1 to s2
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into s1
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):         #Time complexity : O(1)
        # If s1 is empty
        if len(self.s1)==0:
            print("Queue is empty")
            return
        x = self.s1[-1]
        self.s1.pop()
        return x

if __name__ == "__main__":
    Q = Queue()
    Q.enQueue(1)                        
    Q.enQueue(2)                        
    Q.enQueue(3)
    print(Q.deQueue())                        
    print(Q.deQueue())                        
    print(Q.deQueue())                        
    print(Q.deQueue())                        