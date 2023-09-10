import BinaryTree
    
bt = BinaryTree.BinaryTree()
while True:
    value = input('->')
    if value == 'q':
        bt.display_tree()
        break
    bt.insert(int(value))
    
print(bt.search(5))
