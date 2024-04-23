# https://leetcode.cn/problems/implement-queue-using-stacks/description/
# 232. 用栈实现队列
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class MyQueue:

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception("Queue is empty")
        else:
            if self.out_stack.is_empty():
                self.in2out()
            return self.out_stack.pop()

    def peek(self) -> int:
        if self.empty():
            raise Exception("Queue is empty")
        else:
            if self.out_stack.is_empty():
                self.in2out()
            return self.out_stack.peek()

    def empty(self) -> bool:
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def in2out(self):
        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())


# test
myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())  # return 1
print(myQueue.pop())  # return 1, queue is [2]
print(myQueue.pop())  # return 2, queue is []
print(myQueue.empty())  # return True
