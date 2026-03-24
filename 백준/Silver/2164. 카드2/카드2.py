from collections import deque

N = int(input())

queue = deque(range(1, N + 1))

while len(queue) > 1:
    
    queue.popleft() 
    next_card = queue.popleft()
    queue.append(next_card)

print(queue[0])
