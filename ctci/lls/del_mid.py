# Prompt: Implement an algorithm to delete a node in the middle (i.e any
# node but the first and last node, not necessarily the exact middle) of a singly
# linked list, given only access to the first node
from LinkedList import LinkedList

test = LinkedList(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)

expected1 = LinkedList(1)
expected1.append(2)
expected1.append(4)
expected1.append(5)

test.remove_mid()
assert(test == expected1)
