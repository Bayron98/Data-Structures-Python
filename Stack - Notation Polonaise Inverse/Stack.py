class Stack:
    def __init__ (self):
        self.elements = []
    def push(self, data):
        self.elements.append(data)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.elements.pop()
    def is_empty(self):
        return len(self.elements) == 0
