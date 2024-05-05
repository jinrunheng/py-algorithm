class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendLast(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def appendFront(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def deleteFront(self):
        if self.isEmpty():
            raise Exception("DoublyLinkedList is empty")

        # 如果链表中只有一个节点
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            second_node = self.head.next
            second_node.prev = None
            self.head = second_node
        self.size -= 1

    def deleteLast(self):
        if self.isEmpty():
            raise Exception("DoublyLinkedList is empty")
        # 如果链表中只有一个节点
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            penultimate_node = self.tail.prev
            penultimate_node.next = None
            self.tail = penultimate_node
        self.size -= 1

    def isEmpty(self) -> bool:
        return self.size == 0

    def getSize(self) -> int:
        return self.size

    @staticmethod
    def print_list(head):
        if not head:
            print('DoublyLinkedList is empty')
            return
        current = head
        print('None <- ', end="")
        while current:
            # 判断是否是第一个节点，如果不是则：
            if current.prev:
                print(" <-> ", end="")
            print(f"{current.data}", end="")
            current = current.next
            # 如果是最后一个节点，则打印换行
            if not current:
                print(" -> None")
