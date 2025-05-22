from struct_queue import Queue
from struct_stack import Stack
from circular_queue import CircularQueue

def simulate_stack():
    s = Stack()
    s.push(8)
    s.push(7)
    s.push(5)
    s.push(4)
    s.push(3)
    # lanjutkan
    s.pop()
    s.pop()
    s.pop()
    s.push(7)
    s.push(7)
    s.push(5)
    s.push(4)
    s.push(6)
    while not s.is_empty():
        s.pop()
    s.push(5)
    s.push(4)
    s.push(6)
    s.push(4)
    s.push(2)
    s.push(1)

    s.print_stack()


def simulate_queue():
    print("Simulate Queue..")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(6)
    while not q.is_empty():
        q.dequeue()
    q.enqueue(6)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(6)
    q.print_queue()

def simulate_circular_queue():
    cq = CircularQueue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)  # Full now
    cq.display()

    print("Dequeued:", cq.dequeue())
    cq.display()

    cq.enqueue(60)
    cq.dequeue()
    cq.enqueue(65)
    cq.display()

if __name__ == '__main__':
    # please uncomment when you need to enable the simulation stack or queue process
    # simulate_stack()
    simulate_queue()
    # simulate_circular_queue()
