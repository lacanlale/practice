# Prompt: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only needs to be
# right after the elements less than x (see below). The partition element x
# can appear anywhere in the "right partition"; it does not need to appear between
# the left and right partition
# Example: 3,5,8,5,10,2,1 Partion = 5
# Output: 3,1,2,10,5,5,8
from LinkedList import LinkedList

def partition(lst, part:int):
    left_arr = []
    right_arr = []
    n = lst.head
    while n.next != None:
        if n.data >= part:
            right_arr.append(n.data)
        else:
            left_arr.append(n.data)
        n = n.next

    if n.data >= part:
        right_arr.append(n.data)
    else:
        left_arr.append(n.data)

    arr = left_arr + right_arr
    ret_ll = LinkedList(arr.pop(0))
    for i in arr:
        ret_ll.append(i)
    return ret_ll

test = LinkedList(3)
test.append(5)
test.append(8)
test.append(5)
test.append(10)
test.append(2)
test.append(1)

expected = LinkedList(3)
expected.append(2)
expected.append(1)
expected.append(5)
expected.append(8)
expected.append(5)
expected.append(10)

result = (partition(test, 5))
print(result)
assert(result == expected)
