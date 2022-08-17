#단지번호 붙이기 - 그래프 이론

from sys import stdin
from collections import deque

input = stdin.readline


n = int(input().rstrip())

gra = [list(input().rstrip()) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
danji = 0
ans = []


def BFS(x,y):
    cnt = 1
    dq = deque()
    dq.append((x,y))
    visit[x][y] = True
    
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny <n:
                if visit[nx][ny] == False and gra[nx][ny] == '1':
                    visit[nx][ny] = True
                    dq.append((nx,ny))
                    cnt+=1
            else:
                continue
    ans.append(cnt)

for i in range(n):
    for j in range(n):
        if gra[i][j] == '1' and visit[i][j] == False:
            
            BFS(i,j)
            danji+=1    

ans.sort()

print(danji)
print(*ans,sep='\n')


