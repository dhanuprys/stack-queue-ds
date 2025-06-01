from typing import List
from struct_queue import Queue

def sum_front_queues(queue1: Queue, queue2: Queue) -> int|None:
    """
    Menghitung nilai paling depan (first) dari kedua queue.
    
    Args:
        queue1 (Queue): Pointer ke queue pertama
        queue2 (Queue): Pointer ke queue kedua
    
    Returns:
        int|None
    """
    queue1_first = queue1.first()
    queue2_first = queue2.first()
    
    # Jika salah satu queue (queue1 atau queue2) firstnya masih 
    # belum terisi maka fungsi akan me-return None
    if queue1_first is None or queue2_first is None:
        return None
    
    return queue1_first + queue2_first

def sum_last_queues(queue1: Queue, queue2: Queue) -> int|None:
    """
    Menghitung nilai paling belakang (last) dari kedua queue.
    
    Args:
        queue1: Pointer ke queue pertama
        queue2: Pointer ke queue kedua
    
    Returns:
        int|None
    """
    queue1_last = queue1.last()
    queue2_last = queue2.last()
    
    # Jika salah satu queue (queue1 atau queue2) lastnya kosong
    # maka fungsi akan me-return None
    if queue1_last is None or queue2_last is None:
        return None
    
    return queue1_last + queue2_last

def simulate_queue(items: List[int]) -> None:
    even_queue = Queue() # Menyimpan data genap
    odd_queue = Queue() # Menyimpan data ganjil
    
    # Memasukkan data ke dalam queue berdasarkan ganjil genap
    for item in items:
        if item % 2 == 0:
            even_queue.enqueue(item)
        else:
            odd_queue.enqueue(item)
    
    # Menampilkan data apa yang ada saat ini
    even_queue.print_queue()
    odd_queue.print_queue()
    
    # Menghitung depan dan belakang antara 2 queue
    # dan menampilkan hasilnya
    front_sum_result = sum_front_queues(even_queue, odd_queue)
    last_sum_result = sum_last_queues(even_queue, odd_queue)
    print(front_sum_result, last_sum_result)

def main():
    # inputs
    items = [1, 2, 4, 5, 10, 12, 14, 13]
    
    simulate_queue(items)

if __name__ == "__main__":
    main()