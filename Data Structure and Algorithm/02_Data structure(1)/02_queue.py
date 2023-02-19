# Queue data structure
# Queue follows the First In First Out (FIFO) rule 
# In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

# Enqueue: Add an element to the end of the queue
# Dequeue: Remove an element from the front of the queue
# IsEmpty: Check if the queue is empty
# IsFull: Check if the queue is full
# Peek: Get the value of the front of the queue without removing it

# Queue implementation in Python
# Queue implementation in Python


def enqueue(item):
    print("appended",item)
    Queue.append(item)

def is_empty(Queue):
    return len(Queue) == 0

def dequeue():
    if(is_empty(Queue)):
        print(Queue,"Queue is empty")
        return None
    print("First In First Out")
    return Queue.pop(0)

Queue = []
# print(is_empty(Queue))
dequeue()
enqueue(2)
enqueue(3)
enqueue(4)
dequeue()
enqueue(5)

print(Queue)