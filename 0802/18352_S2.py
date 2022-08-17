#특정 거리의 도시 찾기 - 그래프 이론

from sys import stdin
from collections import deque
input = stdin.readline

n,m,k,x = map(int,input().split())
gra = [[]*n for _ in range(n+1)]
#도시 최단거리 초기화
visit = [-1] * (n+1)
#visit의 시작은 -1이 아니라 0
visit[x] = 0
ans = []

for _ in range(m):
    a,b = map(int,input().split())
    gra[a].append(b)

def BFS(x):
    dq = deque([x])
    while dq:       #dq가 빌 때 까지 반복
        a = dq.popleft()
        for i in gra[a]:
            if visit[i] == -1:
                visit[i] = visit[a] + 1
                dq.append(i)
                if visit[i] == k:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        print(*ans,sep='\n')

BFS(x)