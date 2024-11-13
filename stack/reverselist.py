# def reverse_list(lst):
#     r=[]
#     for i in range(len(lst)):
#         r.append(lst.pop())
#     return r
# a=[33,55,66,777]
# result=reverse_list(a)
# print(result)
lst=[8247,928467,293487,76354]

l=[]
for i in lst:
    r=""
    k=list(str(i))
    for _ in range(len(k)):
        r+=k.pop()
    "".join(r)
    l.append(r)
    
print(l)
