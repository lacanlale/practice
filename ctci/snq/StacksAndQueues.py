class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class Stack:
    def __init__(self, data):
        self.head = Node(data)

    def pop(self):
        if self.head == None:
            return None
        top = self.head
        self.head = self.head.next
        return top.data

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        new_top = Node(data)
        old_top = self.head
        
        new_top.next = old_top
        self.head = new_top

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        ret = "["
        n = self.head
        while True:
            ret += str(n) + ','
            if n.next == None:
                break
            n = n.next
        return ret + ']'

class Queue:
    def __init__(self, data):
        self.head = Node(data)

    def __str__(self):
        ret = "["
        n = self.head
        while True:
            ret += str(n) + ','
            if n.next == None:
                break
            n = n.next
        return ret + ']'

    def remove(self):
        top = self.head
        self.head = self.head.next
        return top.data

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
        return n.data

    def isEmpty(self):
        return self.head == None
