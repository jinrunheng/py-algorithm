# 使用列表实现队列
class Queue1:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise Exception('Queue is empty')

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
