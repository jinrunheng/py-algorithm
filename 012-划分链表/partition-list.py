# https://leetcode.cn/problems/partition-list/description/
# 86. 分隔链表
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
