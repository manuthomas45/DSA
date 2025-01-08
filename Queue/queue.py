que=[]
arr=[]
class queue:
    def enqueue(self,data):
        que.append(data)
    def dequeue(self):
        a=que.pop(-1)
        return a
    def reverse(self):
        for i in range(len(que)):
            arr.append(que.pop(-1))
        return arr
    def rec(self):
        if not que:
            return
        print(self.dequeue())
        self.rec()

        


q=queue()
q.enqueue(5)
q.enqueue(2)
q.enqueue(44)
q.enqueue(87)
print(que)
# print(q.reverse())
print(q.rec())
    


















