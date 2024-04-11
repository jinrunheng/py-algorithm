# https://leetcode.cn/problems/add-two-numbers/description/
# 2. 两数相加
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = 0 if val < 10 else 1
            cur_val = val if val < 10 else val - 10
            cur.next = ListNode(cur_val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        carry, cur = self.process(carry, cur, l1)
        carry, cur = self.process(carry, cur, l2)

        if carry: cur.next = ListNode(carry)
        return dummy.next

    def process(self, carry, cur, l):
        while l:
            val = l.val + carry
            carry = 0 if val < 10 else 1
            cur_val = val if val < 10 else val - 10
            cur.next = ListNode(cur_val)
            cur = cur.next
            l = l.next
        return carry, cur
