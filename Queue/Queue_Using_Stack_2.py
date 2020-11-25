# Implementation of queue using two stacks with costly deQueue()
class Queue:
    def __init__(self):
        self.s1 = [] 
        self.s2 = []

    def enQueue(self, x):    #Time complexity : O(1), Auxiliary  space : O(n)
        self.s1.append(x)    

    def deQueue(self):       #Time complexity : O(n)
        # if both the stacks are empty
        if len(self.s2) == 0 and len(self.s1) == 0:
            print("Queue is empty")
            return

        # If s2 is empty and s1 has elements
        if len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1)!=0:
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()    

        else:
            return self.s2.pop()  

if __name__ == "__main__":
    Q = Queue()              
    Q.enQueue(1)
    Q.enQueue(2)
    Q.enQueue(3)

    print(Q.deQueue())
    print(Q.deQueue())
    Q.enQueue(4)
    print(Q.deQueue())
    print(Q.deQueue())
    

            