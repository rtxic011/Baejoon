import sys  # sys 모듈 import

# 명령어 수 입력
N = int(sys.stdin.readline())  # input() -> sys.stdin.readline()

# 배열 기반 덱 초기화
deque = [0] * N * 2
front = N
rear = N

for _ in range(N):
    # input().split() -> sys.stdin.readline().split()
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        front -= 1
        deque[front] = int(cmd[1])

    elif cmd[0] == "push_back":
        deque[rear] = int(cmd[1])
        rear += 1

    elif cmd[0] == "pop_front":
        if front == rear:
            print(-1)
        else:
            print(deque[front])
            front += 1

    elif cmd[0] == "pop_back":
        if front == rear:
            print(-1)
        else:
            rear -= 1
            print(deque[rear])

    elif cmd[0] == "size":
        print(rear - front)

    elif cmd[0] == "empty":
        print(1 if front == rear else 0)

    elif cmd[0] == "front":
        if front == rear:
            print(-1)
        else:
            print(deque[front])

    elif cmd[0] == "back":
        if front == rear:
            print(-1)
        else:
            print(deque[rear - 1])