# Prompt: Given an image represented by an NxN  matrix, where each pixel is 4 bytes,
# write a method to rotate the image 90 degrees. Can you do this in place?

def rotate(img : [[]]) -> [[]]:
    layers = int((len(img)/2)+0.5)
    offset = 0
    for i in range(0, layers):
        for j in range(0, len(img)-1-(offset*2)):
            item1 = img[i][j+offset]
            item2 = img[j+offset][len(img)-1-offset]
            item3 = img[len(img)-1-offset][len(img)-1-j-offset]
            item4 = img[len(img)-1-j-offset][i]

            img[i][j+offset] = item4
            img[j+offset][len(img)-1-offset] = item1
            img[len(img)-1-offset][len(img)-1-j-offset] = item2
            img[len(img)-1-j-offset][i] = item3
        offset += 1
    return img
    

test = [["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"]]
expected = [["m", "i", "e", "a"],
            ["n", "j", "f", "b"],
            ["o", "k", "g", "c"],
            ["p", "l", "h", "d"]]

test2 = [["a", "b", "c"],
         ["d", "e", "f"],
         ["g", "h", "i"]]
expected2 = [["g", "d", "a"],
             ["h", "e", "b"],
             ["i", "f", "c"]]

test3 = [["a", "b"],
         ["c", "d"]]
expected3 = [["c", "a"],
             ["d", "b"]]

assert(rotate(test) == expected)
assert(rotate(test2) == expected2)
assert(rotate(test3) == expected3)
assert(rotate([[]]) == [[]])
