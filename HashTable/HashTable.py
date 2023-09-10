class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
    def hash(self, key, size):
        hashValue = 0
        for char in key:
            hashValue += ord(char)
        return hashValue % size
    def insert(self, key, value):
        entry = HashTableEntry(key, value)
        index = self.hash(key, self.size)
        self.buckets[index] = entry
    def find(self, key):
        index = self.hash(key, self.size)
        if not self.buckets[index]:
            return None
        return self.buckets[index].value
    
