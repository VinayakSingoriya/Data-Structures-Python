#  Program to reverse a stack using recursion
# Recursive function that reverses the given stack using insertAtBottom()
def reverse(stack):
    if (isEmpty(stack)):
        return
    temp = pop(stack)
    reverse(stack)
    insertAtBottom(stack, temp)


# Recursive function that inserts an element at the bottom of a stack
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
        return
    else:
        # Pop elements from stack and keep it in a function call
        topElem = pop(stack)
        insertAtBottom(stack, item)  # push item at bottom
        push(stack, topElem)          # Push all the poped elements in a stack


def createStack():  # Function to initialize a stack
    stack = []
    return stack


def isEmpty(stack):                   # function to check if stack is empty or not
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):  # Function to pop an item from the stack
    if(isEmpty(stack)):  # If stack is empty then error
        print("Stack UnderFlow")
        exit(1)

    return stack.pop()


def prints(stack):  # Function to print the stack
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=" ")
    print()


if __name__ == "__main__":
    stack = createStack()
    push(stack, str(4))
    push(stack, str(3))
    push(stack, str(2))
    push(stack, str(1))
    print("Orignal Stack:")
    prints(stack)
    reverse(stack)
    print("Reversed  stack ")
    prints(stack)
