import heapq#minheap
heap=[]
heapq.heappush(heap,6)
heapq.heappush(heap,1)
heapq.heappush(heap,5)
print(heap)
heapq.heappop(heap)#return smallest elemnt and maintain heap property.deleter min value
print(heap)
lst=[12,34,11,23,54,32,99]
heapq.heapify(lst)#it convert the list to heap 
print(lst)
#heappushpop(it insert the a value and return the smallest element from heap and delete that smallest element)
heapq.heappushpop(lst,66)
print(lst)
#heapreplace(it pop  (and return)smallest element then insert the element)
heapq.heapreplace(lst,88)
print(lst)
#nlargest,nsmallest  these two retrun n largest and n smallest numbers
a=heapq.nsmallest(3,lst)
print(a)
b=heapq.nlargest(4,lst)
print(b)

#
######   priority queue
#element which have smallest value will pop first 
lstt=[(1,"ria"),(4,"siy"),(3,"gia")]
heapq.heapify(lstt)
print(lstt)
c=heapq.heappop(lstt)
print(c)