class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_order_traversal(node):
    """前序遍历：根->左->右"""
    if node is not None:
        print(node.value, end=' ')  # 访问根节点
        pre_order_traversal(node.left)  # 遍历左子树
        pre_order_traversal(node.right)  # 遍历右子树


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

print("前序遍历:")
pre_order_traversal(root)  # 输出: 1 2 4 5 3
