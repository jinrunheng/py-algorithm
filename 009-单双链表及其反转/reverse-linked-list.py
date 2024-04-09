# https://leetcode.cn/problems/reverse-linked-list/
# 206. 反转链表
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

    @staticmethod
    def print_linked_list(head):
        current = head
        while current:
            print(f"{current.val}", end="")
            if current:
                print(" -> ", end="")
            current = current.next
        print('None')


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None

        while head:
            next_node = head.next
            head.next = pre_node
            pre_node = head
            head = next_node
        return pre_node


sol = Solution()
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_linked_list(linked_list.head)
# 1 -> 2 -> 3 -> 4 -> 5 -> None
reversed_head = sol.reverseList(linked_list.head)
linked_list.print_linked_list(reversed_head)
# 5 -> 4 -> 3 -> 2 -> 1 -> None
