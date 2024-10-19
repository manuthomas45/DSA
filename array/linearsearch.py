def l_s(ar,target):
    for i in  ar:
        if i==target:
            return  ar.index(i)
    return "not found"
arr=[3,9,5,7,1,6,49,7]
target=5
print(l_s(arr,target))






# def linear_serch(arr,target):
#     for i in arr:
#         if i == target:
#             return arr.index(i)
#     return -1
# arr=[2,8,4,6,3]
# target=4
# r=linear_serch(arr,target)
# if r!=-1:
#         print(r)
# else:
#         print("not found")
































