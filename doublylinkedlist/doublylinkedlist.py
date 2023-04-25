class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def print(self):
        current_node = self.head
        while current_node.next is not self.head:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print(current_node.data, end=' ')

dllist = DoublyLinkedList()

for i in range(1, 101):
    dllist.add(i)

dllist.print()
