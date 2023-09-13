import LinkedList

class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    #fonction de hachage
    def hash(self, key, size):
        hashValue = 0
        for char in key:
            hashValue += ord(char)
        return hashValue % size
    

    def insert(self, key, value):
        entry = HashTableEntry(key, value)
        index = self.hash(key, self.size)
        lc = self.buckets[index]
        if not lc:
            self.buckets[index] = LinkedList.LinkedList()
            lc = self.buckets[index]
        lc.add(entry)
    def find(self, key):
        index = self.hash(key, self.size)
        lc = self.buckets[index]
        if not lc:
            return None
        return self.findInBucket(lc, key)
    
    def findInBucket(self, lc, key):
        current = lc.head
        while current:
            if current.data.key == key:
                return current.data.value
            current = current.next_node
    

        

    
