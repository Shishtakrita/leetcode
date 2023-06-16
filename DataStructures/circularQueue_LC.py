class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = -1
        self.tail = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        # Enqueue if the queue is not full

        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.head] = 0

        # this means there is only one element, which will be dequeued now
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True

        self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head


if __name__ == '__main__':
    obj = MyCircularQueue(5)
    print(obj.enQueue(3))
    print(obj.deQueue())
    print(obj.queue)
    print(obj.Front())
    print(obj.Rear())
    print(obj.isEmpty())
    print(obj.isFull())
