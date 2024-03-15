from collections import deque

q = deque()


q.append("A")
q.append("B")
q.append("C")

print("Initial queue ")
print(q)

print("\n Element dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\n Queue after removing element")
print(q)