#나이트의 이동 - 그래프이론

from collections import deque


t = int(input())
cnt = 0

dx = [2,2,1,-1,-2,-2,1,-1]
dy = [1,-1,2,2,1,-1,-2,-2]

def BFS(field, start, a):
    dq = deque()
    dq.append(start)

    while dq:
        x,y = dq.popleft()
        for i in range(8):
            mx = dx[i]+x
            my = dy[i]+y

            if a<= mx < 0 or a <= my < 0:
                continue
            if 




for _ in range(t):
    a = int(input())
