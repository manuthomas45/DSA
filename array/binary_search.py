def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "not found"

arr=[4,7,9,1,3,6,8,5]
arr.sort()
target=9

print(binary_search(arr,target))


# --------------------------------usingrecursion

def bin_ser(arr,target,low,high):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return bin_ser(arr,target,mid+1,high)
        else:
            return bin_ser(arr,target,low,mid-1)
    return "not found"
arr=[2,4,6,8,9]
target=8
print(bin_ser(arr,target,0,len(arr)-1))











