# Prompt: Write a program to sort a stack such that the smallest items are on 
# the top. You can use an additional temporary stack but you may NOT copy the
# elements into any other data structure (such as an array). The stack supports
# the following operations: push, pop, peek, and isEmpty.
from StacksAndQueues import Stack

def sort(stk : Stack) -> Stack:
    ret_stk = Stack(stk.pop())
    while True:
        nxt = stk.pop()
        if nxt == None:
            break

        holding = []
        while nxt >= ret_stk.peek():
            holding.append(ret_stk.pop())

        ret_stk.push(nxt)
        for held in holding[::-1]:
            ret_stk.push(held)

    return ret_stk

vals =  [1,2,4,3,2,6,7,10,9,8,11]
test1 = Stack(1)
for val in vals:
    test1.push(val)

sorted_test1 = sort(test1)
print(sorted_test1)

