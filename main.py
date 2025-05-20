from struct_queue import Queue
from struct_stack import Stack

def simulate_stack():
    print("Simulate Stack..")
    stack = Stack()
    stack.push(14)
    stack.push(13)
    stack.push(7)
    stack.push(6)
    stack.push(4)
    stack.push(10)
    stack.sort_stack()


    stack.print_stack()  # Output: 30 -> 20 -> 10 -> None



def simulate_queue():
    print("Simulate Queue..")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.print_queue()  # Output: 10 -> 20 -> 30 -> None

    print("Front before dequeue:", q.first())  # Output: 10

    print("Dequeued:", q.dequeue())  # Output: 10
    q.print_queue()  # Output: 20 -> 30 -> None

    print("Front after dequeue:", q.first())  # Output: 10

if __name__ == '__main__':
    # please uncomment when you need to enable the simulation stack or queue process
    simulate_stack()
    # simulate_queue()
