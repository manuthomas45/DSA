def selection_sort(arr):
    for i in range(0,len(arr)-1):
        cur_min_ind=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[cur_min_ind]:
                cur_min_ind=j
        arr[i],arr[cur_min_ind]=arr[cur_min_ind],arr[i]
arr=[3,12,5,77,12,33,1,2]
selection_sort(arr)
print(arr)
