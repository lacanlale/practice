# Prompt Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we wopuld likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several
# stacks and should create a new stack once the previous one exceeds capcity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Data: {data}"

class Stack:
    def __init__(self, data):
        self.head = Node(data)
        self.len = 0

    def pop(self):
        top = self.head
        self.head = self.head.next
        self.len -= 1
        return top

    def push(self, data):
        new_top = Node(data)
        old_top = self.head
        
        new_top.next = old_top
        self.head = new_top
        self.len += 1

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head == None

class SetofStacks:
    def __init__(self, data, limit):
        self.stack_set = []
        self.limit = limit
        self.stack_set.append(Stack(data))

    def pop(self):
        ret_val = self.stack_set[-1].pop()
        if self.stack_set[-1].len == 0:
            del self.stack_set[-1]
        return ret_val

    def push(self, data):
        pushed = False
        for stck in self.stack_set:
            if stck.len < self.limit:
                pushed = True
                stck.push(data)
                break
        if not pushed:
            self.stack_set.append(Stack(data))

    def peek(self):
        return self.stack_set[-1].peek()

    def isEmpty(self):
        return self.stack_set[-1].isEmpty()

    def popAt(self, index):
        if index > len(self.stack_set):
            return None 
        return self.stack_set[index].pop()
