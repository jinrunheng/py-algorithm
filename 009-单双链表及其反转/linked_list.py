class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    @staticmethod
    def print_linked_list(head):
        current = head
        while current:
            print(f"{current.data}", end="")
            if current:
                print(" -> ", end="")
            current = current.next
        print('None')


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(1)
linked_list.print_linked_list(linked_list.head)
