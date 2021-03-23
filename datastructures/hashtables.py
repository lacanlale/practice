# Ref for exercises:
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md
class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hsh = 0
        for char in key:
            hsh += ord(char)
        return hsh % self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.arr[index].append((key,value))

    def __getitem__(self, key):
        index = self.get_hash(key)
        if len(self.arr[index]) == 1:
            return self.arr[index][0][1]
        else:
            for val in self.arr[index]:
                if val[1] == key:
                    return val[1]

test = HashMap()
test['march 6'] = 10 # Hash val 9
test['march 17'] = 20 # Hash val 9
print(test['march 6'])
print(test['march 17']) 
