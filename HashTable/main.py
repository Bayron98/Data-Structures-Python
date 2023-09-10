import HashTable
def main ():
    ht = HashTable.HashTable(11)
    while True:
            key = input("Enter a key (q for quit): ")
            if key == 'q':
                break
            value = input("Enter a value: ")
            ht.insert(key, value)
    while True:
        key = input("Serch a value in the table (press q to quit): ")  
        if key == 'q':
            break
        value = ht.find(key)
        if value:
            print(value)
        else:
             print('no value found corresponding to the provided key')


main()
