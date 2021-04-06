# Prompt: Implement a function to check if a linked list is a palindrome
from LinkedList import LinkedList

def palindrome(ll : LinkedList) -> bool:
    vals = ll.get_vals()
    mid = int(len(vals)/2)
    left = vals[:mid]
    right = vals[mid:][::-1]
    if len(vals) % 2 == 1:
        right.pop()
    return left == right


test1 = LinkedList('m')
test1.append('o')
test1.append('o')
test1.append('m')

test2 = LinkedList('a')
test2.append('a')
test2.append('a')

test3 = LinkedList('a')
test3.append('a')
test3.append('b')

assert(palindrome(test1) == True)
assert(palindrome(test2) == True)
assert(palindrome(test3) == False)
