class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            print(f'element pushed: {self.head.data}')
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f'element pushed: {new_node.data}')

    def pop(self):
        if self.head is None:
            return 'The stack are empty'
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return 'The stack are empty'
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


stack = Stack()

print(f'are the stack empty: {stack.is_empty()}')
stack.push(10)
stack.push(20)
stack.push(30)
print(f'are the stack empty: {stack.is_empty()}')

print(f'Top element is: {stack.peek()}')

stack.show()
