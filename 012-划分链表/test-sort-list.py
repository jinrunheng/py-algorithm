# https://leetcode.cn/problems/sort-list/description/
# 148. 排序链表
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
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

    # 在这道题的场景下，我们必须使用返回中间节点或中间节点前一个节点的 middleNode 函数
    # 当只有两个节点时，如果我们使用返回中间节点后一个节点，将出现递归死循环，导致栈溢出
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        middle = self.middleNode(head)
        right_head = middle.next
        middle.next = None
        left_sorted_head = self.sortList(head)
        right_sorted_head = self.sortList(right_head)
        return self.mergeTwoLists(left_sorted_head, right_sorted_head)


sol = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
print("原链表：")
sol.print_linked_list(head)
sorted_head = sol.sortList(head)
print("排序后链表：")
sol.print_linked_list(sorted_head)
