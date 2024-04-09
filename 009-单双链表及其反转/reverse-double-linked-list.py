from typing import Optional


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


class Solution:
    def reverseDoubleList(self, head: Optional[DoublyNode]) -> Optional[DoublyNode]:
        pre_node = None
        while head:
            next_node = head.next
            head.next = pre_node
            head.prev = next_node
            pre_node = head
            head = next_node
        return pre_node


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
print('原链表：')
dll.print_list(dll.head)
sol = Solution()
reversed_head = sol.reverseDoubleList(dll.head)
print('反转双向链表：')
dll.print_list(reversed_head)
