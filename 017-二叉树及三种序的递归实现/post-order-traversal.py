class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def post_order_traversal(node):
    """后序遍历：左->右->根"""
    if node is not None:
        post_order_traversal(node.left)  # 遍历左子树
        post_order_traversal(node.right)  # 遍历右子树
        print(node.value, end=' ')  # 访问根节点


# 创建一个简单的二叉树
#       1
#      / \
#     2   3
#    / \
#   4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("后序遍历:")
post_order_traversal(root)  # 输出: 4 5 2 3 1
