class Node:
    def __init__(self, value):
        self.previous_node = Node
        self.next_node = Node
        self.value = value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Ajouter à la fin de la liste
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.previous_node = self.tail
        self.tail.next_node = node
        self.tail = node

    # Ajouter au début de la liste
    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            return
        current_head = self.head
        current_head.previous_node = node
        node.next_node = current_head
        self.head = node

    
    def display(self):
        if not self.head:
            return None
        current = self.head
        while True:
            if(current == self.tail):
               print(current.value, end="\n")
               return
            print(current.value, end="-->")
            current = current.next_node
    def display_backward(self):
        if not self.head:
            return None
        current = self.tail
        while True:
            if(current == self.head):
               print(current.value, end="\n")
               return
            print(current.value, end="-->")
            current = current.previous_node
