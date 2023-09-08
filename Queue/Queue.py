class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0
    def enqueue(self, data):
        self.elements.append(data)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.elements.pop(0)
