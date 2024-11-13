queue=[]
def enqueue():
    element=input("enter the element:")
    queue.append(element)
    print(element,"is added to the queue")
def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e=queue.pop(0)
        print("removed element is",e)
def show():
    print(queue)
enqueue()
enqueue()
enqueue()
dequeue()
show()
# while True:
#     print("select operation 1.add 2.remove 3.show 4.quit")
#     choice =(int(input()))
#     if choice ==1:
#         enqueue()
#     elif choice ==2:
#         dequeue()
#     elif choice ==3:
#         show()
#     elif choice ==4:
#         break
#     else:
#         print("wrong input")

    

        