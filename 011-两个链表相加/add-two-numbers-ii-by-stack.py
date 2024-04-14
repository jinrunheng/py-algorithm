# https://leetcode.cn/problems/lMSNwu/description/
# LCR 025. 两数相加 II
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack = deque()
        stack1 = deque()
        stack2 = deque()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        while stack1 and stack2:
            val = stack1.pop() + stack2.pop() + carry
            carry = 0 if val < 10 else 1
            cur_val = val if val < 10 else val - 10
            stack.append(cur_val)
        while stack1:
            val = stack1.pop() + carry
            carry = 0 if val < 10 else 1
            cur_val = val if val < 10 else val - 10
            stack.append(cur_val)
        while stack2:
            val = stack2.pop() + carry
            carry = 0 if val < 10 else 1
            cur_val = val if val < 10 else val - 10
            stack.append(cur_val)
        if carry: stack.append(carry)

        head_val = stack.pop()
        head = ListNode(head_val)
        cur = head
        while stack:
            val = stack.pop()
            cur.next = ListNode(val)
            cur = cur.next
        return head
