# Prompt: Implement an algorithm to find the kth to last element
# of a singly linked list
from LinkedList import LinkedList

test = LinkedList(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
test.append(6)
test.append(7)

assert(test.get_kth_to_last(6) == 1)
assert(test.get_kth_to_last(5) == 2)
assert(test.get_kth_to_last(4) == 3)
assert(test.get_kth_to_last(3) == 4)
assert(test.get_kth_to_last(2) == 5)
assert(test.get_kth_to_last(1) == 6)
