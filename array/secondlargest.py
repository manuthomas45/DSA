a=[2,7,4,9,1]
m=99
sm=99
for i in range(len(a)):
    # for j in range(i+1,len(a)):
        if a[i]<m:
            t=m
            m=a[i]
            sm=t
        elif a[i]>m and a[i]<sm:
            sm=a[i]
print(sm)
        