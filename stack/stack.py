stack=[]
def push():
    if len(stack)>=n:
        print("stack overflow")
    else:
        element=input("enter a element:")
        stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty!")
    else:
        e=stack.pop()
        print("removed element is:",e)
        print(stack)
n=int(input("enter a limit"))
while True:

    print("select the operation 1. push , 2. pop , 3. quit ")
    choice=int(input())
    if choice ==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter a correct operation!")