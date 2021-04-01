# Prompt: Implement a method to perform basic string compression using the counts 
# of repeated string characters. For example, the string "aabcccccaaa" would become
# "a2b1c5a3". If the compressed string would not become smaller than the original string
# your method should return the original string. You can assume the string has only uppercase and 
# lower case letters (a - z)

def compress(val : str) -> str:
    val = val.strip()
    index = 0
    cmp_str = []
    while index < len(val):
        char = val[index]
        count = 0
        for i in val[index:]:
            if i != char:
                break
            count += 1
        cmp_str.append(f"{char}{count}")
        index += count

    cmp_str = ''.join(cmp_str)
    return cmp_str if len(cmp_str) < len(val) else val 

assert(compress("aabcccccaaa") == "a2b1c5a3")
assert(compress("") == "")
assert(compress("aabbcc") == "aabbcc")
