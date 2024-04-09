# https://leetcode.cn/problems/reverse-linked-list-ii/description/
# 92. 反转链表 II
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def print_linked_list(head: Optional[ListNode]):
        if not head:
            print('LinkedList is empty')
            return
        current = head
        while current:
            print(f"{current.val}", end="")
            if current:
                print(" -> ", end="")
            current = current.next
        print('None')

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        index = 0
        cur_node = dummy_head
        while index != left - 1:
            cur_node = cur_node.next
            index += 1
        before = cur_node
        tail = before.next
        while index != right:
            cur_node = cur_node.next
            index += 1
        after = cur_node.next
        cur_node.next = None

        reversed_head = self.reverse(before.next)
        before.next = reversed_head
        tail.next = after
        return dummy_head.next

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        while head:
            next_node = head.next
            head.next = pre_node
            pre_node = head
            head = next_node
        return pre_node


sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol.print_linked_list(head)
reversed_node = sol.reverseBetween(head, 2, 4)
sol.print_linked_list(reversed_node)
