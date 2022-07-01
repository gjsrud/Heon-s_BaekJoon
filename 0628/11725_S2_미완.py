#트리의 부모 찾기 - 그래프

n = int(input())
gra = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]

def DFS(gra,start)


for _ in range(n):
    x,y = map(int,input().split())
    gra[x-1][y-1] = 1

