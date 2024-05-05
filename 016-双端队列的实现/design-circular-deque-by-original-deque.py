from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.my_deque = deque(maxlen=k)
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if len(self.my_deque) < self.capacity:
            self.my_deque.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.my_deque) < self.capacity:
            self.my_deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.my_deque) == 0:
            return False
        else:
            self.my_deque.popleft()
            return True

    def deleteLast(self) -> bool:
        if len(self.my_deque) == 0:
            return False
        else:
            self.my_deque.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.my_deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.my_deque[-1]

    def isEmpty(self) -> bool:
        return len(self.my_deque) == 0

    def isFull(self) -> bool:
        return len(self.my_deque) == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(10)
obj.insertFront(3)
obj.insertFront(2)
obj.insertLast(1)
obj.insertLast(9)
obj.deleteFront()
obj.deleteLast()
print(obj.getFront())  # 3
print(obj.getRear())  # 1
print(obj.isEmpty())  # False
print(obj.isFull())  # False
obj.deleteLast()
obj.deleteFront()
print(obj.getFront())  # -1
print(obj.getRear())  # -1
print(obj.isEmpty())  # True
print(obj.isFull())  # False
