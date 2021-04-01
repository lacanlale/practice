# Prompt: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire column are set to 0

def zero_it(mat : [[]]) -> [[]]:
    # r x c
    cols = set()
    for ind_i, i in enumerate(mat):
        for ind_j, j in enumerate(i):
            if j == 0:
                cols.add(ind_j)

    for col in cols:
        for i in range(0, len(mat)):
            mat[i][col] = 0
    return mat


test1 = [[1, 2, 3],
         [0, 2, 3],
         [1, 2, 3]]
expected1 = [[0, 2, 3],
            [0, 2, 3],
            [0, 2, 3]]

test2 = [[0]]
expected2 = [[0]]

test3 = [[1],
         [2],
         [0],
         [4]]
expected3 = [[0],
             [0],
             [0],
             [0]]

assert(zero_it([[]]) == [[]])
assert(zero_it(test1) == expected1)
assert(zero_it(test2) == expected2)
assert(zero_it(test3) == expected3)
