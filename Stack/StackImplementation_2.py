# Implementation of Stack using collection.deque
from collections import deque
stack = deque()

# Pushing element into stack
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)


print("poping elements from the stack")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack after all the elements are poped")
print(stack)
