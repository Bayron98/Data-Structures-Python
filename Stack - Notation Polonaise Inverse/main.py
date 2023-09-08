import Stack

stack = Stack.Stack()
while(True):
    data = input('->')
    if(data == '+' or data == '-' or data == '/' or data == '*'):
        n1 = stack.pop()
        n2 = stack.pop()
        res = eval(f'{n1} {data} {n2}')
        stack.push(res)
    elif(data == 'f'):
        print(stack.elements)
        break
    else:
        stack.push(data)



