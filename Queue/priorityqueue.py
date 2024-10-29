# In priorityqueue   each element associated with priority.  based on priority it will remove from  the queue
#based on there values
q=[]
q.append(30)
q.append(10)
q.append(20)
q.append(50)
q.sort()
q.pop(0)
q.pop(0)
print(q)

# -----------------------------implemeneting with priorityqueuefuntion-----------
import queue
q=queue.PriorityQueue()
q.put(10)
q.put(90)
q.put(90)
q.put(50)
q.put(60)
a=q.get()#10
b=q.get()#50
c=q.get()#60
print(c)
#priority fuction will  prioritise based on the value  if there is same value then it  remove based on the index

# ---------------prirority assinging in tuple here the highest  value  have highest priority
que=[]
que.append((1,"alexa"))
que.append((4,"alex"))
que.append((2,"alexander"))
que.sort(reverse=True)
print(que)
d=que.pop(0)
print(d)
que.pop(0)