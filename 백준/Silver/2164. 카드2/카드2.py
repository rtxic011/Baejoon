# O(1) 연산을 위해 deque 모듈 임포트 (문제 조건 분석과 일치)
from collections import deque

# 카드의 개수 입력
N = int(input())

# 1부터 N까지의 정수를 큐(deque)에 저장
# queue = deque([1, 2, 3, ..., N])
queue = deque(range(1, N + 1))

# 카드가 한 장 남을 때까지 (즉, 큐의 길이가 1보다 클 때 동안) 반복
while len(queue) > 1:
    
    # 맨 위 카드 버리기 (제거)
    # 큐의 맨 앞에서 원소를 제거 (O(1) 연산)
    queue.popleft() 
    
    # 다음 카드를 맨 아래로 이동
    # 현재 맨 위 카드(제거되지 않은)를 꺼내서 (O(1) 연산)
    next_card = queue.popleft()
    # 큐의 맨 뒤에 추가 (O(1) 연산)
    queue.append(next_card)

# 마지막 남은 카드 출력
# 큐의 길이가 1이므로, 첫 번째(0번 인덱스) 원소를 출력
print(queue[0])
