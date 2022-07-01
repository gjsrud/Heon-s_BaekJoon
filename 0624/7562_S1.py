#나이트의 이동 - 그래프이론

from collections import deque

'''
0으로 가득찬 그래프를 만들고
처음 시작을 1로 적어둠
탐색을 계속 진행하여 계속 해서 그래프에 숫자를 1씩 더하여 적어줌
결국 s_x,s_y가 e_x,e_y와 같으면 -1하고 종료
'''

t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

#s_x,s_y,e_x,e_y
# a는 x, b는 y // x는 mx, y는 my

def BFS(s_x,s_y,e_x,e_y):
    dq = deque()
    dq.append([s_x,s_y])
    gra[s_x][s_y] = 1

    while dq:
        x,y = dq.popleft()

        if x == e_x and y == e_y:
            print(gra[e_x][e_y]-1)
            return

        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            if 0<=mx<size and 0<=my<size and gra[mx][my]==0:
                dq.append([mx,my])
                gra[mx][my]=gra[x][y]+1
        
for _ in range(t):
    size = int(input())
    s_x,s_y = map(int,input().split())
    e_x,e_y = map(int,input().split())
    gra = [[0]*size for _ in range(size)]
    BFS(s_x,s_y,e_x,e_y)