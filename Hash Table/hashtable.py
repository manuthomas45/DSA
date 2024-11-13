# class Hashtabel:
#     def __init__(self):
#         self.Max=100
#         self.arr=[None for i in range(self.Max)]
#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h+=ord(char)
#         return h%self.Max
#     def add(self,key,val):
#         h=self.get_hash(key)
#         self.arr[h]=val
#     def get(self,key):
#         h=self.get_hash(key)
#         return self.arr[h]

# t=Hashtabel()
# t.add('march 6',130)
# print(t.arr)
# print(t.get('march 6'))
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Simple hash function (modulus operation)
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]  # Create a new list if empty
        else:
            # Collision resolution logic here
            self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None
h=HashTable(10)
h.insert("march9",5)
print(h.get("march9"))