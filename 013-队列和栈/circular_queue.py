class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    """
    打印循环队列
    """

    def print_queue(self):
        if self.is_empty():
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

    """
    入队操作
    """

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    """
    出队操作
    """

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    """
    判断循环队列是否为空
    """

    def is_empty(self):
        return self.size == 0

    """
    判断循环队列是否已满
    """

    def is_full(self):
        return self.size == self.capacity


circular_queue = CircularQueue(3)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
print("init ... capacity 为 3 的循环队列")
print("append 1")
print("append 2")
print("append 3")
print("打印循环队列：")
circular_queue.print_queue()
print("弹出队首元素")
circular_queue.dequeue()
circular_queue.print_queue()
print("append 4")
circular_queue.enqueue(4)
circular_queue.print_queue()
