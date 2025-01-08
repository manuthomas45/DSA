class MinHeap:
    def init(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_minimum(self):
        return self.heap[0] if self.heap else None

    def insert(self, data):
        self.heap.append(data)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)

        minimum = i

        if left < len(self.heap) and self.heap[left] < self.heap[minimum]:
            minimum = left

        if right < len(self.heap) and self.heap[right] < self.heap[minimum]:
            minimum = right

        if minimum != i:
            self.swap(i, minimum)
            self.min_heapify(minimum)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.min_heapify(0)

        return root


arr = [1, 5, 7, 3, 7, 2, 5, 8]
min_heap = MinHeap()
for i in arr:
    min_heap.insert(i)

print(min_heap.heap)
min_heap.extract_min()
print(min_heap.heap)