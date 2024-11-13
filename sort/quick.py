def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Sample usage
elements = [11, 9, 29, 0, 23, 11333, 876, 2, 6, 7, 2, 15, 28]
quick_sort(elements, 0, len(elements) - 1)
print("Sorted array:", elements)
