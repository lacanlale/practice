# Prompt: Given two (singly) linked lists, determine if two lists intersect.
# Return the intersecting node. Note that the intersection is defined based
# on reference, not value. That is, if the kth node of the first linked list
# is the exact same node (by reference) as the jth node of the second list, then
# they are interesecting
from LinkedList import LinkedList, Node

def has_intersect(l1: LinkedList, l2: LinkedList):
    m = l1.head
    while True:
        n = l2.head
        while True:
            if m is n:
                return m
            if n.next == None:
                break
            n = n.next
        if m.next == None:
            break
        m = m.next
    return None



a = Node(1)
test1_val1 = LinkedList(2)
test1_val1.head.next = a
test1_val2 = LinkedList(3)
test1_val2.head.next = a

assert(has_intersect(test1_val1, test1_val2) is a)
