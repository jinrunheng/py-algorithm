# https://leetcode.cn/problems/merge-two-sorted-lists/
# 21. 合并两个有序链表
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 if list1 is not None else list2
        head = list1 if list1.val <= list2.val else list2
        cur1 = head.next
        cur2 = list2 if head == list1 else list1
        cur = head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 if cur1 is not None else cur2
        return head


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


sol = Solution()

list1 = LinkedList()
list2 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)
print("list1:")
sol.print_linked_list(list1.head)

list2.append(1)
list2.append(3)
list2.append(5)
print("list2:")
sol.print_linked_list(list2.head)

head = sol.mergeTwoLists(list1.head, list2.head)
print("merged linked list:")
sol.print_linked_list(head)
