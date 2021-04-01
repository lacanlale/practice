# Prompt: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two strings
# write a function to check if they are one edit (or zero edits away)
# Example:
#   pale, pale -> true
#   pales, pale -> true
#   pale, bake -> false

def one_away(str1 : str, str2 : str) -> bool:
    str1 = str1.strip()
    str2 = str2.strip()
    if str1 == str2:
        return True
    if abs(len(str1) - len(str2)) >= 2:
        return False

    diffs = 0
    for ind, ch in enumerate(str1):
        if ind < len(str2) and ch != str2[ind]:
            diffs += 1

    return diffs <= 1 

assert(one_away("pale", "bake") == False)
assert(one_away("", "ke") == False)
assert(one_away("abc", "de") == False)
assert(one_away("abcde", "de") == False)
assert(one_away("de", "abcde") == False)

assert(one_away("", "a") == True)
assert(one_away("abc", "ab") == True)
assert(one_away("pale", "pale") == True)
assert(one_away("pales", "pale") == True)
