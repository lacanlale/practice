# Prompt: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limted to just dictionary words
# Ex:
#   Input: Tact Coa
#   Output: True

# Brute force: Generalize all permutations until that permutation is a palindrome
# Better: Sort the string and try to create two ends of a palindrome
# Runtime improvement => O(n!n) => O(2n + log(n))
def is_palindrome(val:str) -> bool:
    val = sorted(val.lower().replace(' ','')) # O(log(n))
    odds = 0
    counts = {}
    for i in val:
        counts[i] = val.count(i) # O(n)

    for i in counts.values(): # O(n)
        if i%2 != 0:
            odds += 1

    if len(val) %2 == 0 and odds != 0:
        return False
    elif len(val) %2 != 0 and odds != 1:
        return False
    return True


assert(is_palindrome("ab") == False)
assert(is_palindrome("bbbbac") == False)

assert(is_palindrome("a") == True)
assert(is_palindrome("Tact Coa") == True)
assert(is_palindrome("") == True)
assert(is_palindrome("aaaa") == True)
assert(is_palindrome("moonoom") == True)
assert(is_palindrome("baaab") == True)
