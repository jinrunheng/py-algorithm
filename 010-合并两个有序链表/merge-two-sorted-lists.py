# https://leetcode.cn/problems/merge-two-sorted-lists/
# 21. 合并两个有序链表
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
