from struct_node import Node
from typing import Optional

class Stack:
    def __init__(self):
        self.top: Optional[Node] = None  # top pointer to the stack

    def push(self, data: int):
        new_node = Node(data=data, next=self.top)
        self.top = new_node  # top now points to the new node

    def pop(self) -> Optional[int]:
        if self.top is None:
            return None
        popped_value = self.top.data
        self.top = self.top.next  # move the top pointer to the next node
        return popped_value

    def peek(self) -> Optional[int]:
        return self.top.data if self.top else None

    def is_empty(self) -> bool:
        return self.top is None

    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
