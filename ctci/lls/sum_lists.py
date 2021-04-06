# Prompt: You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that the
# 1's digit is at the head of the list. Write a function that adds the two nubmers
# and returns the sum as a linked list
# Example
#   Input (7 -> 1 -> 6) + (5 -> 9 -> 2) == 617 + 295
#   Output 2 -> 1 -> 9 == 912
from LinkedList import LinkedList
def get_int_val_rev(l1:LinkedList) -> int:
    return int(''.join(map(str,l1.get_vals()[::-1])))

def reverse_sum(l1: LinkedList, l2: LinkedList) -> LinkedList :
    val1 = int(''.join(map(str,l1.get_vals()[::-1]))) 
    val2 = int(''.join(map(str,l2.get_vals()[::-1]))) 
    sum_val = str(val1+val2).split()[::-1]
    n = LinkedList(sum_val.pop(0))
    for i in sum_val:
        n.append(int(i))
    return n

test1_val1 = LinkedList(7)
test1_val1.append(1)
test1_val1.append(6)
test1_val2 = LinkedList(5)
test1_val2.append(9)
test1_val2.append(2)

assert(get_int_val_rev(reverse_sum(test1_val1, test1_val2)) == 912)

# Follow up
# Suppose the digits are stored in forward order. Repeat the above problem
# Example
#   Input (6 -> 1 -> 7) + (2 -> 9 -> 5) == 617 + 295
#   Output 9 -> 1 -> 2 == 912
def sum_norm(l1: LinkedList, l2: LinkedList) -> LinkedList :
    val1 = int(''.join(map(str,l1.get_vals()))) 
    val2 = int(''.join(map(str,l2.get_vals()))) 
    sum_val = str(val1+val2).split()
    n = LinkedList(sum_val.pop(0))
    for i in sum_val:
        n.append(int(i))
    return n
     

def get_int_val(l1:LinkedList) -> int:
    return int(''.join(map(str,l1.get_vals())))

test1_val1 = LinkedList(6)
test1_val1.append(1)
test1_val1.append(7)
test1_val2 = LinkedList(2)
test1_val2.append(9)
test1_val2.append(5)

assert(get_int_val(sum_norm(test1_val1, test1_val2)) == 912)

