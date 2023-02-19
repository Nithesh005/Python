# A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

# In programming terms, putting an item on top of the stack is called push and removing an item is called pop.

# Basic Operations of Stack:
#     * Push: Add an element to the top of a stack
#     * Pop: Remove an element from the top of a stack
#     * IsEmpty: Check if the stack is empty
#     * IsFull: Check if the stack is full
#     * Peek: Get the value of the top element without removing it

stack = []

def push(stack,data):
    stack.append(data)
    print("the pushed data is : " ,data)

def check_empty(stack):
    return len(stack) == 0


push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)

if(check_empty(stack)):
    print("Stack is empty")
else:
    print(stack.pop())
print(stack)


