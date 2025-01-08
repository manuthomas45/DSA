class Heap:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)//2
    def left_child(self,i):
        return (i*2)+1
    def rigth_child(self,i):
        return (i*2)+2
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def length(self):
        return len(self.heap)
    def get_max(self):
        return self.heap[0] if self.heap else None
    def insert(self,key):
        self.heap.append(key)
        current=self.length()-1
        while current>0 and self.heap[current]>self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current=self.parent(current)
    def max_heapify(self,i):
        left=self.left_child(i)
        right=self.rigth_child(i)
        largest=i
        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left
        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right
        if largest!=i:
            self.swap(i,largest)
            self.max_heapify(largest)
    def extract_max(self):
        if len(self.heap)==0:
            return None
        root=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        if len(self.heap)>0:
            self.max_heapify(0)
        return root
    def heap_sort(self):
        sorted_array=[]
        while self.length()>0:
            sorted_array.append(self.extract_max())
        print(sorted_array)
    def delete_key(self,index):
        print(self.heap[index])
        if index >=len(self.heap) or index<0:
            return None
        self.heap[index]=self.heap[-1]
        self.heap.pop()
        if index<len(self.heap):
            self.max_heapify(index)
        


max_heap=Heap()
num=[36.86,12,98,394,56,43,65]
for i in num:
    max_heap.insert(i)
print(max_heap.heap)
a=max_heap.extract_max()

print(a)
max_heap.delete_key(3)
max_heap.heap_sort()