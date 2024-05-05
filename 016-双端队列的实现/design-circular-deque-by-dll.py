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


class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.dll = DoublyLinkedList()

    def insertFront(self, value: int) -> bool:
        if self.dll.getSize() < self.capacity:
            self.dll.appendFront(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.dll.getSize() < self.capacity:
            self.dll.appendLast(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.dll.deleteFront()
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.dll.deleteLast()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dll.head.data

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dll.tail.data

    def isEmpty(self) -> bool:
        return self.dll.isEmpty()

    def isFull(self) -> bool:
        return self.dll.getSize() == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(10)
obj.insertFront(3)
obj.insertFront(2)
obj.insertLast(1)
obj.insertLast(9)
obj.deleteFront()
obj.deleteLast()
print(obj.getFront())  # 3
print(obj.getRear())  # 1
print(obj.isEmpty())  # False
print(obj.isFull())  # False
obj.deleteLast()
obj.deleteFront()
print(obj.getFront())  # -1
print(obj.getRear())  # -1
print(obj.isEmpty())  # True
print(obj.isFull())  # False
