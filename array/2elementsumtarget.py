arr=[2,3,4,5,6,9]
t=11
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==t:
#             print ([arr[i],arr[j]])


            # ---------------O(n^2)
            # ---------------O(n)

s=set()
for i in  arr:
    k=t-i
    if k in s:
        print ([i,k])
    s.add(i)
