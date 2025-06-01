from typing import List
from struct_stack import Stack

def insert_reversed_unique_item(stack: Stack, items: List[int]) -> None:
    """
    Menambahkan data non-duplikat ke dalam stack.

    Args:
        stack (Stack): Pointer untuk stack yang akan diisi.
        items (List[int]): Daftar items yang akan dimasukkan ke dalam stack.

    Returns: None
    """
    used = []
    
    # Membuat perulangan traversal pada items
    for i in range(len(items)):
        # Jika item saat ini (items[i]) belum pernah dimasukkan
        # ke dalam stack, maka tambahkan ke dalam stack
        if items[i] not in used:
            stack.push(items[i])
            used.append(items[i])

def count_total_items(stack: Stack) -> int:
    """
    Menghitung jumlah dari item yang tersimpan pada stack.
    Pada fungsi ini saya mencoba 3 cara, yaitu:
    1. menggunakan pop
    2. menggunakan fungsi to_array() yang sudah bapak sediakan
    3. mengakses langsung property top (sering digunakan pada beberapa method di dalam)
    
    Saya memilih cara nomor 2 karena cara nomor 1 akan menghapus semua item
    tersimpan (sedangkan di ketentuan tidak ada keterangan untuk menghapus data), dan
    cara nomor 3 rasanya kurang tepat karena harus mengakses property langsung dari
    kelas Stack yang saya rasa kurang lazim.
    
    Args:
        stack (Stack): Pointer stack
    
    Returns: 
        int: Jumlah items yang tersimpan pada stack
    """
    # 1. Menggunakan metode pop (downside: akan menghapus semua data di-stack)
    # result = 0
    # while not stack.is_empty():
    #     result += stack.pop()
    # return result
    
    # 2. Menggunakan fungsi to_array() yang ada pada code base
    result = 0
    for item in stack.to_array():
        result += item
    return result

    # 3. Mengakses property top secara langsung
    # result = 0
    # current = stack.top
    # while current:
    #     result += current.data
    #     current = current.next
    # return result

def simulate_stack(items: List[int]) -> None:
    stack = Stack()
    
    # Memasukkan data ke dalam stack dan memfilter data duplikat
    insert_reversed_unique_item(
        stack=stack,
        items=items
    )
    
    # Sorting stack secara ascending
    stack.sort_stack()
    # Menampilkan data stack saat ini
    stack.print_stack()
    
    # Menghitung jumlah total dari items yang ada pada stack
    total = count_total_items(stack)
    print(total)

def main():
    # inputs
    items = [2, 3, 4, 5, 10, 12, 5, 4, 5, 2]
    
    simulate_stack(items)
    
if __name__ == "__main__":
    main()