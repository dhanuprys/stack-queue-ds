from struct_node import Node
from typing import Optional

class Queue:
    def __init__(self):
        self.head: Optional[Node] = None  # pointer to the front node
        self.tail: Optional[Node] = None   # pointer to the rear node

    def enqueue(self, data: int):
        new_node = Node(data=data)
        if self.tail is None:
            # Queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # link new node at end of queue
            self.tail = new_node       # move rear to new node

    def dequeue(self) -> Optional[int]:
        if self.head is None:
            return None  # Queue is empty
        dequeued_value = self.head.data
        self.head = self.head.next  # move front to next node
        if self.head is None:
            self.tail = None  # if queue becomes empty
        return dequeued_value

    def first(self) -> Optional[int]:
        return self.head.data if self.head else None

    def is_empty(self) -> bool:
        return self.head is None

    def print_queue(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
