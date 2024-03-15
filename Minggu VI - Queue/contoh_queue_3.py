from  queue import Queue

q = Queue(maxsize=3)

print(q.qsize())

q.put("A")
q.put("B")
q.put("C")

print("\n Full : ",q.full())

print("\n Elements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())


print("\n empty : ",q.empty())

q.put(1)
print("\n Empty : ",q.empty())
print("\n Full : ",q.full())