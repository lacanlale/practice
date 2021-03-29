# Prompt: Given two strings, write a method to decide if one is a permutation of the other
def check_perm(val1 : str, val2 : str) -> bool:
    copy_1 = sorted(val1)
    copy_2 = sorted(val2)
    return copy_1 == copy_2 
    

assert(check_perm("aaa","bbb") == False)
assert(check_perm("aaa","bab") == False)
assert(check_perm("","bbb") == False)

assert(check_perm("","") == True)
assert(check_perm("aaa","aaa") == True)
assert(check_perm("abc","bca") == True)
