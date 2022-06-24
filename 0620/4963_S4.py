#섬의 개수 - 그래프 이론

from collections import deque

ans = []

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]

def BFS(field, start):
    dq = deque()
    dq.append(start)

    while dq:
        x,y = dq.popleft()
        for i in range(8):
            mx = dx[i]+x
            my = dy[i]+y
            #print(field[mx][my])
            if 0<=mx<h and 0<=my<w:
                if field[mx][my] == 1 and visit[mx][my] == 0:
                    visit[mx][my] = 1
                    dq.append((mx,my))


while True:
    w, h = map(int,input().split())
    visit = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    field = []

    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        num = list(input().split())
        num = list(map(int,num))
        field.append(num)

    for i in range(h):
        for k in range(w):
            if field[i][k] == 1 and visit[i][k] == 0:
                BFS(field,(i,k))
                count += 1
    
    ans.append(count)

print(*ans,sep='\n')
