class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        removed = self.queue[self.front]
        if self.front == self.rear:  # Hanya satu elemen
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        index = self.front
        print("Queue contents:", end=" ")
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print()
