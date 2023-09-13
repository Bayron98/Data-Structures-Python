import DoublyLinkedList
def main():
    dl =  DoublyLinkedList.DoublyLinkedList()
    while True:
        entry = input('(q pour quitter)Entrez une valeur: ')
        if entry == 'q':
            break
        dl.append(entry)
    dl.display()
    dl.display_backward()
main()