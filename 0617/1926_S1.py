# 그림 - 그래프 이론


from collections import deque
from sys import stdin

n,m = map(int,stdin.readline().rstrip().split())

paint = []
w_list = []

for _ in range(n): #paint 끝
    num = list(stdin.readline().rstrip().split())
    num = list(map(int,num)) #문자열을 int형으로
    paint.append(num)

visit = [[0 for _ in range(m)] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(paint, start):
    dq = deque()
    dq.append(start)
    width=0
    while dq:
        x,y = dq.popleft()
        
        for i in range(4):
            mx = dx[i]+x
            my = dy[i]+y
            if 0<=mx<n and 0<=my<m:
                if paint[mx][my] == 1 and visit[mx][my]==0:
                    visit[mx][my] = 1
                    dq.append((mx,my))
                    width += 1

    return width                    

#start에 들어갈 값

count = 0

#n은 세로 / m은 가로

for k in range(n):
    for i in range(m):
        if paint[k][i] == 1 and visit[k][i] == 0:
            #BFS(paint,(i,k))
            w_list.append(BFS(paint,(k,i)))
            count+=1


print(count)
if len(w_list) == 0:
    print(0)
elif sum(w_list) == 0:
    print(1)
else:
    print(max(w_list))


