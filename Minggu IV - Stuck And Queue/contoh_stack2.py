from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('stack')
print(stack)

print('\nElement yang dihapus dari stack:')
print(stack.pop())


print('\nStack setelah elements di hapus:')
print(stack)