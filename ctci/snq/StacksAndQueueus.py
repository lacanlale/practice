class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Data: {data}"

class Stack:
    def __init__(self, data):
        self.head = Node(data)

    def pop(self):
        top = self.head
        self.head = self.head.next
        return top

    def push(self, data):
        new_top = Node(data)
        old_top = self.head
        
        new_top.next = old_top
        self.head = new_top

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        ret = ""
        n = self.head
        while True:
            ret += str(n)
            if n.next == None:
                break
            n = n.next
        return ret

class Queue:
    def __init__(self, data):
        self.head = Node(data)

    def __str__(self):
        ret = ""
        n = self.head
        while True:
            ret += str(n)
            if n.next == None:
                break
            n = n.next
        return ret

    def remove(self):
        top = self.head
        self.head = self.head.next
        return top

    def add(self, data):
        n = self.head
        while True:
            if n.next == None:
                break
            n = n.next
        n.next = Node(data)

    def peek(self):
        n = self.head
        while True:
            if n.next != None:
                break
            n = n.next
        return n

    def isEmpty(self):
        return self.head == None
