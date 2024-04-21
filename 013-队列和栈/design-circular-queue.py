# https://leetcode.cn/problems/design-circular-queue/
# 622. 设计循环队列
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [-1] * self.capacity
        self.size = 0
        self.head = 0
        self.tail = 0

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
