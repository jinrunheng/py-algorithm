class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

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


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_list(dll.head)
