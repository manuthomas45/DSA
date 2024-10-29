def bubble_sort(arr):
    for i in range (len(arr)-1):
        m=0
        # if we want to stop it after a iteration then crate a variable here and check if it is chaged after the
        # j for loop .if it is not changed then may be it is sorted so we can stop (break)it.
        # in each iteration in j the last element will be placed in the order only the last element so i
        #  implimented m variable we can write it without m also . we get same output
        for j in range(len(arr)-i-1-m):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        m+=1
arr=[2,99,44,3,55,9,45,23,0]
bubble_sort(arr)
print(arr)











