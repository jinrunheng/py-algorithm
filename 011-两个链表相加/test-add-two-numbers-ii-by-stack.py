# https://leetcode.cn/problems/lMSNwu/description/
# LCR 025. 两数相加 II
from collections import deque
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


sol = Solution()
ln1 = LinkedList()
ln1.append(7)
ln1.append(2)
ln1.append(4)
ln1.append(3)
print("链表 l1：")
sol.print_linked_list(ln1.head)

ln2 = LinkedList()
ln2.append(5)
ln2.append(6)
ln2.append(4)
print("链表 l2：")
sol.print_linked_list(ln2.head)

l = sol.addTwoNumbers(ln1.head, ln2.head)
print("相加链表 l：")
sol.print_linked_list(l)
