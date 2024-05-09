class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_traversal(node):
    """中序遍历：左->根->右"""
    if node is not None:
        in_order_traversal(node.left)  # 遍历左子树
        print(node.value, end=' ')  # 访问根节点
        in_order_traversal(node.right)  # 遍历右子树


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

print("中序遍历:")
in_order_traversal(root)  # 输出: 4 2 5 1 3
