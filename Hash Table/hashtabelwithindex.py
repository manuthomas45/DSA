class Hashtabel:
    def __init__(self):
        self.Max=100
        self.arr=[None for i in range(self.Max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

t=Hashtabel()
t["march 9"]=20
t["march 10"]=23
t["march 11"]=45
t["march 12"]=75
t["march 13"]=39
print(t.arr)
print(t['march 9'])
print(t['march 10'])
del t["march 12"]
print(t['march 12'])