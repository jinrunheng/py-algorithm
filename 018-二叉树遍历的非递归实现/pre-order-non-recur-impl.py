# 144. 二叉树的前序遍历
# https://leetcode.cn/problems/binary-tree-preorder-traversal
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res

        stack = [root]
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.right is not None:
                stack.append(pop.right)
            if pop.left is not None:
                stack.append(pop.left)
        return res
