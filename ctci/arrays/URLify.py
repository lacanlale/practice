# Prompt: Write a method to replace all spaces in a string with '%20'
# You may assume that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string. 
# Example:
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

def urlify(val : str, true_len : int) -> str:
    val = val.strip()
    return val.replace(' ', '%20')


assert(urlify("Mr John Smith   ", 13) == "Mr%20John%20Smith")
assert(urlify("", 0) == "")
assert(urlify("    ", 0) == "")
assert(urlify(" 0 ", 1) == "0")
assert(urlify(" 0  0", 1) == "0%20%200")
