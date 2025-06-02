from typing import List
from circular_queue import CircularQueue

def extend_queue_with_pattern(
    current_queue: CircularQueue,
    prev_queue_size: int,
    new_items: List[int]
) -> CircularQueue:
    """
    Fungsi ini akan menggabungkan antara queue lama dengan items yang baru.
    
    Pola penggabungan:
    new_items[0] + ...current_queue items... + new_items[1-n]
    
    new_items[0] -> item pertama pada new_items
    current_queue items -> semua items yang ada pada queue saat ini
    new_items[1-n] -> semua items yang ada pada new_items namun dimulai dari index 1,
                    karena index 0 sudah digunakan di awal.
    
    Args:
        current_queue (CircularQueue): CircularQueue saat ini
        prev_queue_size (int): Panjang/kapasitas dari current_queue
        new_items (List[int]): Daftar items yang akan digabungkan
        
    Returns: CircularQueue instance baru dari hasil penggabungan
    """
    new_items_len = len(new_items)
    
    # Jika panjang items yang baru adalah 0 atau kebawah alias kosong
    # maka tidak akan ada operasi yang dilakukan dan program hanya
    # mengembalikan objek dari queue sebelumnya
    if new_items_len <= 0:
        return current_queue
    
    new_cq_size = prev_queue_size + new_items_len
    new_cq = CircularQueue(new_cq_size)
    
    # new_items[0]
    new_cq.enqueue(new_items[0])
    # current_queue items
    while not current_queue.is_empty():
        new_cq.enqueue(current_queue.dequeue())
    # new_items[1-n]
    for i in range(1, new_items_len):
        new_cq.enqueue(new_items[i])
        
    return new_cq

def simulate_circular_queue(items: List[int], next_items: List[int]) -> None:
    # Initial capacity untuk CircularQueue yang akan dibuat
    cq_size = len(items)
    cq = CircularQueue(cq_size)
    
    # Memasukkan seluruh elemen pada items ke dalam queue
    for item in items:
        cq.enqueue(item)
    
    # Menggabungkan queue saat ini dengan next_items dengan pola
    # yang sudah ditentukan (untuk polanya dijelaskan pada 
    # dokumentasi fungsi di bawah)
    cq = extend_queue_with_pattern(
        current_queue=cq,
        prev_queue_size=cq_size,
        new_items=next_items
    )
    cq.print_circular_queue()

def main():
    # inputs
    items = [5, 4, 3, 2, 10]
    next_items = [11, 12, 13, 14]
    
    simulate_circular_queue(items, next_items)

if __name__ == "__main__":
    main()