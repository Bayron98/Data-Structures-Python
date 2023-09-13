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
    value = input('Which value do you wich to delete: ')
    if dl.delete(value):
            print('deletion succeded')
            dl.display()
            dl.display_backward()
main()