# Prompt: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?
def is_unique(val : str) -> bool:
    copy = val
    for i in val:
        copy = copy[1:]
        if i in copy:
            return False
    return True


assert(is_unique("aaaa") == False), f"Input: 'aaaa' should be False"
assert(is_unique("bbaa") == False), f"Input: 'abab' should be False"
assert(is_unique("abab") == False), f"Input: 'abab' should be False"

assert(is_unique("") == True), f"Input: '' should be False"
assert(is_unique("abcd") == False), f"Input: 'abcd' should be False"
