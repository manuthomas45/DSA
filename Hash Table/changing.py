class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
    def get_hash(self,key):
        return sum(ord(count) for count in key)%self.size
    def __setitem__(self,key,val):
        index=self.get_hash(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i]=(key,val)
                return
        self.table[index].append((key,val))
    def __getitem__(self,key):
        index=self.get_hash(key)
        for k,v in self.table[index]:
            if k==key:
                return v
        return None
    def __delitem__(self,key):
        index=self.get_hash(key)
        self.table[index]=[(k,v) for k,v in self.table[index] if k!=key]
    

    
h=Hashtable(5)
h["march 17"]=2
h["march 17"]=5
h["march 6"]=5
h["march 22"]=5
# h.__delitem__("march 22")
del h["march 22"]
# print(h.__getitem__("march 22"))
print(h["march 6"])
print(h.table)
print(h.get_hash("march 6"))