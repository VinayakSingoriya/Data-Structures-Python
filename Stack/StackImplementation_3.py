# Stack Implementation using queue module
from queue import LifoQueue

# Initialize a Stack
stack = LifoQueue(maxsize=3)

print("Initial size of stack:", stack.qsize())

# Pushing elements in the Stack
stack.put(1)
stack.put(2)
stack.put(3)

print("Full: ", stack.full())
print("size: ", stack.qsize())

# poping elements from the stack
print("Elements poped from the stack:")
print(stack.get())
print(stack.get())
print(stack.get())

print("\n Empty: ", stack.empty())