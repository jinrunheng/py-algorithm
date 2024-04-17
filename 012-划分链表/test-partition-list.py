from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)


class Solution:

    @staticmethod
    def print_linked_list(head: Optional[ListNode]):
        current = head
        while current:
            print(f"{current.val}", end="")
            if current:
                print(" -> ", end="")
            current = current.next
        print('None')

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_part = ListNode(-1)
        right_part = ListNode(-1)
        left_cur = left_part
        right_cur = right_part
        while head:
            if head.val < x:
                left_cur.next = head
                head = head.next
                left_cur = left_cur.next
                left_cur.next = None
            else:
                right_cur.next = head
                head = head.next
                right_cur = right_cur.next
                right_cur.next = None

        left_cur.next = right_part.next
        return left_part.next


sol = Solution()
linkedList = LinkedList()
linkedList.append(4)
linkedList.append(3)
linkedList.append(2)
linkedList.append(5)
linkedList.append(1)
print("初始链表：", end='')
sol.print_linked_list(linkedList.head)
print("特定值 x：", 3)
print("分割链表：", end='')
partition_head = sol.partition(linkedList.head, 3)
sol.print_linked_list(partition_head)
