import collections
stack =collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

a=stack.pop()
stack.append(a)
print(stack[-1])
# collection is a module and deque is a class.we use this calss as stack
print(stack)