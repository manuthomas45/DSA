def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            elements[start], elements[end] = elements[end], elements[start]
    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


elements = [11, 9, 29, 0, 23, 11333, 876, 2, 6, 7, 2, 15, 28]
quick_sort(elements, 0, len(elements) - 1)
print("Sorted array:", elements)
