# Queue is an another class and in there LifoQueue is a calss in that moduel we can use this class for create stack
# in Queue put for push and get for pop
import queue
stack=queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40,timeout=1)
stack.get()