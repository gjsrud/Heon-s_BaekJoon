#유기농 배추 - 그래프이론

'''


'''



def BFS(graph,start):
    dq = deque()
    dq.append(start)

    while dq:

        x,y = dq.popleft()
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if 0<=mx<n and 0<=my<m:
                if graph[mx][my] == 1 and visit[mx][my] == 0:
                    visit[mx][my] = 1
                    dq.append((mx,my))


from collections import deque


t = int(input())

field = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for _ in range(t):
    m,n,k = map(int,input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x,y= map(int,input().split())
        field[y][x] = 1

    count = 0

    for k in range(m):
        for i in range(n):
            if field[i][k] == 1 and visit[i][k] == 0:
                BFS(field,(i,k))
                count +=1
    
    print(count)















'''
그래프의 모든 부분에 BFS처리가 필요하다
'''