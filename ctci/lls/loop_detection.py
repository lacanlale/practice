# Prompt: Given a cicular linked lsit, implement an alogrithm that 
# returns the node at the beginning of the loop

# I dont have the implementation they had for circular so im winging it

def get_loop_node(ll):
    seen = []
    n = ll.head
    while True:
        for i in seen:
            if i is n:
                return i
        if n.next == None:
            break
        n = n.next
        seen.append(n)
    return None
