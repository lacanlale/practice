# Prompt: Write code to remove duplicates from an unsorted linked list
# Follow up
# How would you solve this problem if a temporary buffer is not allowed
from LinkedList import LinkedList

test1 = LinkedList(1)
test1.append(1)
test1.append(2)
test1.append(2)
test1.append(2)
test1.append(3)
test1.append(3)

expected1 = LinkedList(1)
expected1.append(2)
expected1.append(3)

test1.remove_dups()
print(test1)
assert(test1 == expected1)
