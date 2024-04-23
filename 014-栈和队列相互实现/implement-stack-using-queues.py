# https://leetcode.cn/problems/implement-stack-using-queues/
# 225. 用队列实现栈
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def peek(self):
        if not self.is_empty():
            peek_val = self.queue.popleft()
            self.queue.appendleft(peek_val)
            return peek_val
        else:
            raise Exception('Queue is empty')

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


class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        size = self.q.size()
        self.q.enqueue(x)
        i = 0
        while i < size:
            self.q.enqueue(self.q.dequeue())
            i += 1

    def pop(self) -> int:
        if self.empty():
            raise Exception('Stack is empty')
        return self.q.dequeue()

    def top(self) -> int:
        if self.empty():
            raise Exception('Stack is empty')
        return self.q.peek()

    def empty(self) -> bool:
        return self.q.is_empty()


# test
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  # 2
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.empty())  # True
