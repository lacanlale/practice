# Prompt: 
# Given a smaller string s and a bigger string b, design an algorithm to find all
# permutations of the shorter strign within the longer one. Print the location of each 
# permutation

# Brute force method: find all permutations of s and check if any permutation exists in b
#   Runtime: O(s! * b)

# Better method (but not the only good one)
# O(bs)
def get_perm_loc(s, b):
    count = 0

    inc = len(s)
    for ind, _ in enumerate(b):
        sub = list(b[ind : ind+inc])
        stack_s = list(s)
        if ind+inc > len(b):
            break

        for char in s:
            if char in sub:
                sub.remove(char)
                stack_s.remove(char)

        if len(stack_s) == 0:
            count += 1
    print(f"{count} permutation matches found")

s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"
get_perm_loc(s, b)
