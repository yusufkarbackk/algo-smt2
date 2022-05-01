class SinglyLinkedList:  # kelas untuk membuat linked list
    def __init__(self):
        self.head = None  # nilai awal head adalah none

    def __str__(self):
        result = ""
        pointer = self.head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result

    def add_first(self, element):
        newNode = _Node(element)  # membuat objek dari kelas Node
        # isi nextNode dari node yang baru berisi nilai dari head
        newNode.nextNode = self.head
        self.head = newNode  # head di perbarui dengan node yang baru


class _Node:  # kelas untuk membuat node
    def __init__(self, element):
        self.element = element
        self.nextNode = None



myList = SinglyLinkedList()
myList.add_first(10)
myList.add_first(20)
myList.add_first(30)

print(str(myList))



