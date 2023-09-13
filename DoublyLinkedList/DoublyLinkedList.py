class Node:
    def __init__(self, value):
        self.previous_node = None
        self.next_node = None
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

    def delete(self, value):
        if not self.head:
            return None
        current = self.head
        found = False
        while current:
            if current.value == value:
                found = True
                break
            current = current.next_node
        if not found:
            return None
        before_current = current.previous_node
        after_current = current.next_node
        if not before_current:
            self.head = after_current
            after_current.previous_node = None
        elif not after_current:
            self.tail = before_current
            before_current.next_node = None
        else:
            before_current.next_node = after_current
            after_current.previous_node = before_current
        return True
