class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return

        if self.is_empty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity

        self.queue[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        removed = self.queue[self.head]
        if self.head == self.tail:  # Hanya satu elemen
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity

        return removed

    def first(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.head]

    def last(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.last]

    def print_circular_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        index = self.head
        while True:
            print(self.queue[index], end="")
            if index == self.tail:
                break
            print(" -> ", end="")
            index = (index + 1) % self.capacity
        print()
