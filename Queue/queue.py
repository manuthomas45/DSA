def enqueue(val):
    queue.append(val)
def dequeue():
    queue.pop(0)
    
queue=[]
enqueue(5)
enqueue(6)
enqueue(98)
enqueue(58)
dequeue()
print(queue)