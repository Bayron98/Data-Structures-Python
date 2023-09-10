class Node:
    def __init__(self, value):
        self.value = value
        self.LeftChildNode = None
        self.RightChildNode = None


class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if node.value < current.value:
                    if not current.LeftChildNode:
                        current.LeftChildNode = node
                        return
                    else:
                        current  = current.LeftChildNode
                else:
                    if not current.RightChildNode:
                        current.RightChildNode = node
                        return
                    else:
                        current  = current.RightChildNode
    
    def display_inorder(self, node):
        if node:
            self.display_inorder(node.LeftChildNode)
            print(node.value)
            self.display_inorder(node.RightChildNode)

    def display_tree(self):
        if self.root:
            self.display_inorder(self.root)
    
    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return current
            elif current.value < value:
                current = current.RightChildNode
            else:
                current = current.LeftChildNode
        return None