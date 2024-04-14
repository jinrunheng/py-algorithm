# https://leetcode.cn/problems/add-two-numbers/description/
# 2. 两数相加
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


sol = Solution()
ln1 = LinkedList()
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

print("相加后的链表：")
l = sol.addTwoNumbers(ln1.head, ln2.head)
sol.print_linked_list(l)
