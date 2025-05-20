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

    def to_array(self):
        arr = []
        current = self.top
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    def sort_stack(self):
        temp_stack = Stack()

        while not self.is_empty():
            # Step 1: Pop element from original stack
            tmp = self.pop()

            # Step 2: Move elements back to original if they are bigger than tmp
            while not temp_stack.is_empty() and temp_stack.peek() < tmp:
                self.push(temp_stack.pop())

            # Step 3: Push tmp to temp_stack
            temp_stack.push(tmp)

        # Step 4: Copy back from temp_stack to self to preserve ascending order
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
