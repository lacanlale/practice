# Prompt: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
# only one call to is_rotation (e.g. "waterbottle" is a rotation of "erbottlewat").

def is_rotation(s1 : str, s2 : str) -> bool:
    if s1 == s2:
        return True

    div = 0 
    for ind_i, _ in enumerate(s2):
        if not s2[0:ind_i] in s1:
            break
        div = ind_i

    left = s2[0:div]
    right = s2[div:]
    if s1 == right+left:
        return True
    return False


assert(is_rotation("waterbottle", "erbottlewat") == True)
assert(is_rotation("waterbottle", "waterbottle") == True)
assert(is_rotation("waterbottle", "ttlewaterbo") == True)
assert(is_rotation("", "") == True)

assert(is_rotation("cat", "dog") == False)
