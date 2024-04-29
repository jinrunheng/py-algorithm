# 使用列表实现栈
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


class MinStack:

    def __init__(self):
        self.data_stack = Stack()
        self.min_stack = Stack()

    def push(self, val: int) -> None:
        self.data_stack.push(val)
        if self.min_stack.is_empty():
            self.min_stack.push(val)
        else:
            cur_min = self.min_stack.peek()
            self.min_stack.push(cur_min) if cur_min < val else self.min_stack.push(val)

    def pop(self) -> None:
        if self.data_stack.is_empty():
            raise Exception("Stack is empty")
        self.data_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.data_stack.is_empty():
            raise Exception("Stack is empty")
        return self.data_stack.peek()

    def getMin(self) -> int:
        if self.min_stack.is_empty():
            raise Exception("Stack is empty")
        return self.min_stack.peek()
