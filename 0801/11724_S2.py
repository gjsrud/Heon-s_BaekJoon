#연결 개수의 개수 - 그래프 이론


from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int, input().split())

gra = [[]*m for _ in range(n+1)]
visit = [False for _ in range(n+1)]
count = 0

for _ in range(m):
    u,v = map(int, input().split())
    gra[u].append(v)
    gra[v].append(u)

def BFS(v):
    dq = deque([v])
    visit[v] = True

    while dq:
        v = dq.popleft()

        for i in gra[v]:
            if not visit[i]:
                dq.append(i)
                visit[i] = True

for i in range(1,n+1):
    if not visit[i]:
        BFS(i)
        count+=1

print(count)

'''
만약 v가 1이면
visit = [False],[True],[False]...
dq = [1]
gra[1] = [2,5]
i는 2,5
i가 2 -> visit[2]는 False
dq.append(2,5)
visit[2] = True
visir[5] = True

'''