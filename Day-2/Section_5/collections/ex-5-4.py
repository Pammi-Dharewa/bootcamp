from collections import deque

d = deque()
d.appendleft('first')  # queue: enqueue
d.appendleft('second')
print(d.pop())         # stack: pop → 'first'
