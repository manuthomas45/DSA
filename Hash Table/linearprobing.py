class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:  # Linear probing for collision resolution
            if self.table[index][0] == key:
                break  # Update value if key already exists
            index = (index + 1) % self.size  # Wrap around if end is reached
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Key found
            index = (index + 1) % self.size
            if index == start_index:
                break  # Full loop completed
        return None  # Key not found

    def display(self):
        for i, entry in enumerate(self.table):
            print(f"Index {i}: {entry}")

# Example usage:
hash_table = HashTable(5)
hash_table.insert(10, "A")
hash_table.insert(15, "B")
hash_table.insert(20, "C")
hash_table.insert(25, "D")  # Collision occurs, resolved with linear probing
hash_table.display()

print("Search for key 15:", hash_table.search(15))
print("Search for key 30:", hash_table.search(30))
