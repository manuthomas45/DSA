class Queue:
    def init(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self,data):
        self.queue.pop(0)
        
    def display(self):
        print(self.queue)
        
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue(2)
queue.display()