class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def get_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update if key exists
                return
        self.table[index].append((key, value))  # Add new if key not found

    def __getitem__(self, key):
        index = self.get_hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Return None if key not found

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

# Example usage
t = HashTable()
t["march 25"] = 99
t["march 17"] = 87
t["march 6"] = 34
print(t.table)  # View entire table
print(t["march 25"])  # Access specific key
print(t["march 17"])
print(t["march 6"])

# del t["march 17"]  # Delete a key
print(t.table)  # View updated table


# # 2 methods
# #1 chaning
# # 2linear probing
# # here i implementd chaning

# class Hashtable:
#     def __init__(self):
#         self.Max=10
#         self.arr=[[] for i in range(self.Max)]
#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h+=ord(char)
#         return h%self.Max
#     def __setitem__(self,key,val):
#         h=self.get_hash(key)
#         found=False
#         for idx,element in enumerate(self.arr[h]):
#             if  element[0]==key:
#                 self.arr[h][idx]=(key,val)
#                 found=True
#                 break
#         if not found:
#             self.arr[h].append((key,val))
#     def __getitem__(self,key):
#         h=self.get_hash(key)
#         # return self.arr[h] it return the list of tuple result in the same h value
#         for element in self.arr[h]:
#             if element[0]==key:
#                 return element[1]
#     def __delitem__(self,key):
#         h=self.get_hash(key)
#         for index,element in enumerate(self.arr[h]):
#             if element[0]==key:
#                 del self.arr[h][index]   
# t=Hashtable()
# t["march 25"]=99
# t["march 17"]=87
# t["march 6"]=34
# print(t.arr)
# print(t["march 25"])
# print(t.get_hash("march 25"))
# print(t["march 17"])
# print(t["march 6"])
# # del t["march 17"]
# # del t["march 6"]
# print(t.arr)