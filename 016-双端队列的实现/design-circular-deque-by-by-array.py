class MyCircularDeque:

    def __init__(self, k: int):
        self.my_list = [0] * k
        self.capacity = k
        self.size = 0
        self.left, self.right = 0, 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.my_list[0] = value
        else:
            self.my_list[(self.left + self.capacity - 1) % self.capacity] = value
            self.left = (self.left + self.capacity - 1) % self.capacity
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.my_list[0] = value
        else:
            self.my_list[(self.right + 1) % self.capacity] = value
            self.right = (self.right + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.left = 0
            self.right = 0
        else:
            self.left = (self.left + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.left = 0
            self.right = 0
        else:
            self.right = (self.right + self.capacity - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.my_list[self.left]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.my_list[self.right]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


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
