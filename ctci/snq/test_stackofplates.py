import SetofStacks as s

vals = [2,3,4,5,6]
stack = s.Stack(1)
for i in vals:
    stack.push(i)

set_stacks = s.SetofStacks(1)
for i in vals:
    set_stacks.push(i)

assert(set_stacks.pop() == stack.pop())
assert(set_stacks.peek() == stack.peek())
