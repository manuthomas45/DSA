arr=[1,2,4,3,7,3,9,3]
t=3
i=0
j=len(arr)-1
while i<j:
    if arr[i]==t and arr[j]!=t:
        arr[i],arr[j]=arr[j],arr[i]
    elif arr[i]!=t:
        i+=1
    elif arr[j]==t:
        j-=1
print(arr)
