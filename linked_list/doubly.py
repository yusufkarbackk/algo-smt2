
# kelas untuk membuat sebuah node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# kelas untuk membuat sebuah double linked list


class Doubly_linked_list:
    def __init__(self):
        self.head = None #node

    # adding data elements
    def append(self):
        data = int(input('masukan data: '))
        if self.head is None:  # cek apakah head saat ini kosong
            new_node = Node(data)  # membuat objek node
            new_node.prev = None  # variabel prev dari node di isi None
            self.head = new_node  # head linked list sekarang di isi dengan node pertama
        else:  # head tidak kosong
            new_node = Node(data)  # membuat objek node
            current = self.head  # head yang sekarang dimasukan dalam variabel current
            while current.next != None:  # loop selama next tidak none
                current = current.next
            current.next = new_node  # next dari current di isi dengan node sekarang
            new_node.prev = current  # prev dari node sekarang di isi dengam current
            new_node.next = None  # next dari node sekarang berisi none

    def listprint(self):
        current = self.head
        while current != None:
            print(current.data)

            current = current.next

# 8 12


dllist = Doubly_linked_list()
dllist.append()
dllist.append()
dllist.append()
dllist.listprint()
