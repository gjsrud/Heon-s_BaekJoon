'''
BFS사용
'''

from sys import stdin

n, m = map(int, stdin.readline().split())

'''
1과0이 아니고
maze[0][0]에서 maze[n-1][m-1]로 봐야함
'''

maze = []

for _ in range(n): #미로 완성
    num = list(stdin.readline().rstrip())
    maze.append(num)

dx = [-1,1,0,0] #위로 올라가려면 숫자를 하나 줄여야함 d[1]이 d[2]보다 위 칸임
dy = [0,0,-1,1] #왼쪽으로 가려면 숫자를 하나 줄여야함
dq = [[0,0]] #start지점

maze[0][0] = 1

while dq:
    x,y = dq[0][0], dq[0][1]

    del dq[0]
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx >= 0 and my >= 0 and mx<n and my<m:
            if maze[mx][my] == "1":
                dq.append([mx,my])
                maze[mx][my] = maze[x][y] + 1



print(maze[n-1][m-1])
