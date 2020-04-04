# Stacks use LIFO standard, but Queues uses FIFO which means
# First In First Out. To work with queues we need deque module from
# python colletions module
from collections import deque

queues = deque([])
queues.append(1)
queues.append(2)
queues.append(3)
print(queues)
queues.popleft()
print(queues)
if not queues:
    print("Empty")
