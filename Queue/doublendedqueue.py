import collections
q=collections.deque()#create a emptyqueue
print(q)

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)
q.pop()
print(q)
#-------------------second method

que=collections.deque()
que.append(10)
que.append(10)
que.append(10)
que.append(10)
print(que)
que.popleft()
que.popleft()
que.popleft()
print(que)
