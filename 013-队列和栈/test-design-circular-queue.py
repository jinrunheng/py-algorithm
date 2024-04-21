# https://leetcode.cn/problems/design-circular-queue/
# 622. 设计循环队列
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [-1] * self.capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def print_queue(self):
        if self.isEmpty():
            print("head [] tail")
            return

        # 确定打印的起始和结束位置
        start = self.head

        # 构建要打印的队列元素列表
        queue_elements = []
        for i in range(start, self.capacity):
            if self.queue[i] is not None:
                queue_elements.append(str(self.queue[i]))
        for i in range(0, start):
            if self.queue[i] is not None:
                queue_elements.append(str(self.queue[i]))

        print(f'head [{",".join(queue_elements)}] tail')

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.queue[self.head] = -1
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[(self.tail - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


print("初始化队列：")
obj = MyCircularQueue(3)  # 创建一个容量为 3 的循环队列
print("append 1")
print("---->", obj.enQueue(1))  # 返回 True，队列变为 [1, -1, -1]
print("append 2")
print("---->", obj.enQueue(2))  # 返回 True，队列变为 [1, 2, -1]
print("append 3")
print("---->", obj.enQueue(3))  # 返回 True，队列变为 [1, 2, 3]
print("打印队列：")
obj.print_queue()
print("append 4，超出队列容量")
print("---->", obj.enQueue(4))  # 返回 False，队列已满
print("查看队尾元素：")
print("---->", obj.Rear())  # 返回 3，队尾元素
print("判断列队是否已满：")
print("---->", obj.isFull())  # 返回 True，队列已满
print("出队一个元素：")
print("---->", obj.deQueue())  # 返回 True，队列变为 [-1, 2, 3]，队首元素 1 出队
print("打印队列：")
obj.print_queue()
print("查看队尾元素：")
print("---->", obj.Rear())  # 返回 3
print("append 4")
print("---->", obj.enQueue(4))  # 返回 True，队列变为 [4, 2, 3]
obj.print_queue()
print("查看队尾元素")
print("---->", obj.Rear())  # 返回 4，队尾元素
