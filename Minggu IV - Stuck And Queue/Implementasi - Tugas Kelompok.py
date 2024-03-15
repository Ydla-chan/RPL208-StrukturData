class Stack:
    def __init__(self):
        # Inisialisasi stack dengan list kosong
        self.items = []

    def is_empty(self):
        # Memeriksa apakah stack kosong
        return len(self.items) == 0

    def push(self, item):
        # Menambahkan elemen ke dalam stack
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            # Menghapus dan mengembalikan elemen teratas dari stack
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            # Mengembalikan elemen teratas tanpa menghapusnya
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        # Mengembalikan jumlah elemen dalam stack
        return len(self.items)

class Queue:
    def __init__(self):
        # Inisialisasi queue dengan list kosong
        self.items = []

    def is_empty(self):
        # Memeriksa apakah queue kosong
        return len(self.items) == 0

    def enqueue(self, item):
        # Menambahkan elemen ke dalam queue
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            # Menghapus dan mengembalikan elemen paling depan dari queue
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            # Mengembalikan elemen paling depan tanpa menghapusnya
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        # Mengembalikan jumlah elemen dalam queue
        return len(self.items)
# Contoh penggunaan Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack Size:", stack.size())
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack is empty?", stack.is_empty())

# Contoh penggunaan Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue Size:", queue.size())
print("Front element:", queue.front())
print("Dequeued element:", queue.dequeue())
print("Queue is empty?", queue.is_empty())