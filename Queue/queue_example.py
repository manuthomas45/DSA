# FiFO methodology
# enqueue --> add element to queue
# dequeue --> delete element from queue
# isFull to chech queue is full or not
# isEmpty is used to chech the queue is empty or not
queue=[]
queue.append(10)
queue.append(20)
queue.append(130)

queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)
print(not queue)
# ------------------------change the front and rare each other
q=[]
q.insert(0,60)
q.insert(0,50)
q.insert(0,40)
print(q)
q.pop()
print(q)