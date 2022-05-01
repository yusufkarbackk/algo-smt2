# kelas untuk membuat node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# kelas untuk membuat circular linked list


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = None

    def append(self, data):  # fungsi untuk menambahkan node
        if self.head == None:  # jika nilai awal head adalah none
            self.head = Node(data)  # head di isi dengan node
            self.head.next = self.head  # nilai next pada head akan menunjuk head kembali
        else:  # jika nilai head tidak none
            new_node = Node(data)  # membuat objek Node
            current = self.head  # head disimpan dalam variabel current

            '''
             # loopin selama nilai next tidak menunjuk kepada head
             yang berarti sudah ada di akhir list
            '''
            while current.next != self.head:
                current = current.next  # variabel current di isi dengan Node sebelahnya
            current.next = new_node  # next dari node terakhir menunjuk ke node yang baru
            new_node.next = self.head  # next dari node yang baru menunjuk ke head

    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
            if current == self.head:
                break


myList = CircularLinkedList()

myList.append(10)
myList.append(20)
myList.append(40)



myList.printList()
