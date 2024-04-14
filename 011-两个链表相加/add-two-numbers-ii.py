# https://leetcode.cn/problems/lMSNwu/description/
# LCR 025. 两数相加 II
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        pre_node = None

        while head:
            next_node = head.next
            head.next = pre_node
            pre_node = head
            head = next_node
        return pre_node

    def addTwoNumbersI(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_reverse = self.reverseList(l1)
        l2_reverse = self.reverseList(l2)
        l_reverse = self.addTwoNumbersI(l1_reverse, l2_reverse)
        return self.reverseList(l_reverse)
