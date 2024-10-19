def sum_of_list(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+sum_of_list(arr[1:])
arr=[3,7,2,8]
print(sum_of_list(arr))