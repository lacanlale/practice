# Prompt: Implement a MyQueue class which implements a queue using two stacks
from StacksAndQueues import *

class MyQueue:
    def __init__(self, data):
        self.stack1 = Stack(Node(data))
        self.stack2 = None

    def stack_to_queue(self):
        if self.stack2 == None:
            self.stack2 = Stack(self.stack1.pop())

        while True:
            val = self.stack1.pop()
            if val == None:
                break
            self.stack2.push(val)

    def queue_to_stack(self):
        self.stack1 = Stack(self.stack2.pop())
        while True:
            val = self.stack2.pop()
            if val == None:
                break
            self.stack1.push(val)

    def add(self, data):
        self.stack1.push(data)

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

    def remove(self):
        self.stack_to_queue()
        return_val = self.stack2.pop()
        self.queue_to_stack()
        return return_val.data

    def peek(self):
        self.stack_to_queue()
        return_val = self.stack2.peek()
        self.queue_to_stack()
        return return_val.data


vals = [2,3,4,5]
normal_q = Queue(1)
for val in vals:
    normal_q.add(val)

stack_queue = MyQueue(1)
for val in vals:
    stack_queue.add(val)

assert(normal_q.peek() == stack_queue.peek())
assert(normal_q.isEmpty() == stack_queue.isEmpty())
assert(normal_q.remove() == stack_queue.remove())
