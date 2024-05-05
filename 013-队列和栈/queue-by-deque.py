# 使用双端队列（deque）实现队列
from collections import deque


class Queue2:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise Exception('Queue is empty')

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
