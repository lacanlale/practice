class Node:
    def __init__(self, data, nxt=None):
        self.data = data 
        self.next = nxt 

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def __str__(self):
        n = self.head
        offset = 2
        ret_str = ""
        while n.next != None:
            ret_str += (f"Data:{n.data} => \n{' '*offset}")
            n = n.next
            offset += 2
        ret_str += (f"Data:{n.data} => NONE")
        return ret_str

    def __eq__(self, l2):
        if l2 == None: 
            return False
        self_vals = self.get_vals()
        l2_vals = l2.get_vals()
        return self_vals == l2_vals

    def combine(self, l2):
        n = self.head
        while n.next != None:
            n = n.next
        n.next = l2.head

    # Remove dups Q2.1
    def remove_dups(self):
        ## O(n+n)
        n = set(self.get_vals())
        self.head = Node(n.pop())
        for i in n:
            self.append(i)
    
    # Remove dups Q2.3
    def remove_mid(self):
        ## O(n+n)
        n = self.get_vals()
        if len(n)%2 == 0:
            return
        del n[int(len(n)/2)]
        self.head = Node(n.pop())
        for i in n:
            self.append(i)

    def get_vals(self):
        ret = []
        n = self.head
        while n.next != None:
            ret.append(n.data)
            n = n.next
        ret.append(n.data)
        return ret
    
    # Kth to Last Q2.2
    def get_kth_to_last(self, ind):
        # O(n) time & space
        return self.get_vals()[-ind]

    def append(self, val: int):
        n = self.head
        while n.next != None:
            n = n.next
        n.next = Node(val)
