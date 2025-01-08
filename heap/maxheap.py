class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return (i * 2) + 1
    
    def right_child(self, i):
        return (i * 2) + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def length(self):
        return len(self.heap)
    
    def get_max(self):
        return self.heap[0] if self.heap else None
    
    def insert(self, key):
        self.heap.append(key)
        
        current = self.length()-1
        
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def max_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        
        largest = i
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
            
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]
        
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if len(self.heap) > 0:
            self.max_heapify(0)
            
        return root
    
    def increase_key(self, i, new_value):
        
        self.heap[i] = new_value
        
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def delete_key(self, key):
        if 0 <= key < self.length():
            self.increase_key(key, float('inf'))
            
            self.extract_max()
    
    def heap_sort(self):
        sorted_array = []
        while self.length() > 0:
            sorted_array.append(self.extract_max())
        return sorted_array
    
    def build_max_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        
        for i in range(n // 2 -1, -1, -1):
            self.max_heapify(i)
    
    def replace_max(self, new_val):
        root = self.heap[0]
        
        self.heap[0] = new_val
        
        self.max_heapify(0)
        
        return root

    def delete_key(self, index):
        if index >= len(self.heap) or index < 0:
            return None  # Index out of bounds

        # Replace the element to be deleted with the last element
        self.heap[index] = self.heap[-1]
        self.heap.pop()  # Remove the last element

        # Restore the heap property
        if index < len(self.heap):  # Only if the heap is not empty
            self.max_heapify(index)
        
        return True  # Indicate successful deletion


# Example Usage
max_heap = MaxHeap()

# Insert elements into the max-heap
elements = [10, 20, 5, 6, 1, 8, 12]
for el in elements:
    max_heap.insert(el)

print("Max Heap after insertion:", max_heap.heap)  # Print the current state of the heap
print("Maximum element:", max_heap.get_max())  # Get the maximum element
print("Extracted max:", max_heap.extract_max())  # Extract the maximum element
print("Max Heap after extraction:", max_heap.heap)  # Print the heap after extraction

# Increase key operation
max_heap.increase_key(2, 25)
print("Max Heap after increasing key at index 2 to 25:", max_heap.heap)

# Delete key operation
max_heap.delete_key(3)  # Delete the key at index 3
print("Max Heap after deleting key at index 3:", max_heap.heap)

# Heap sort operation
sorted_array = max_heap.heap_sort()
print("Sorted array:", sorted_array)  # Print the sorted array
