stack = []


def push(data):
    stack.append(data)
    print(f'Element pushed: {data}')


def pop():
    if is_empty():
        return 'The stack is empty'
    else:
        stack.pop()


def peek():
    if is_empty():
        print('The stack is empty')
    else:
        print(f'Top element is: {stack[-1]}')


def is_empty():
    return len(stack) < 1


def show():
    index = len(stack)-1
    while index >= 0:
        print(stack[index])
        index -= 1


push(10)
push(5)
push(6)
peek()
show()
