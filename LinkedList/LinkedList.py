class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return 
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = node
    def display(self):
        current = self.head
        while current:
            print(current.data, end='-->')
            current = current.next_node
        print('None')