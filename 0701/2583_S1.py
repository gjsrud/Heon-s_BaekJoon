# 영역 구하기 - 그래프 이론

from collections import deque

m,n,k = map(int,input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
a = 0


def BFS(y,x):
    dq = deque()
    dq.append((y,x))
    cnt = 1
    gra[y][x] = 1
    while dq:
        a,b = dq.popleft()
        for i in range(4):
            mx = dx[i]+b
            my = dy[i]+a
            if 0<=mx<n and 0<=my<m and gra[my][mx] == 0:
                    gra[my][mx] = 1
                    dq.append((my,mx))
                    cnt+=1
    return cnt



# m = 세로(y), n = 가로(x)
gra = [[0]*n for _ in range(m)]

#gra완성 필요
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    a = x1
    while True:
        gra[y1][a]=1
        if a == x2-1 and y1==y2-1:
            break
        if y1 != y2-1:
            if a != x2-1:
                a+=1
            elif a == x2-1:
                a = x1
                y1+=1
        elif y1 == y2-1:
            if a != x2-1:
                a+=1
            elif a == x2-1:
                continue

#print(gra)

for i in range(m):
    for j in range(n):
        if gra[i][j] == 0:
            gra[i][j] = 1
            ans.append(BFS(i,j))

ans.sort()
print(len(ans))
print(*ans,sep=' ')
