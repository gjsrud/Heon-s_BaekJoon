#상근이의 여행 - 그래프 이론
#이건 bfs를 한줄 짜리네 더 쉽네
from collections import deque
from sys import stdin

t = int(stdin.readline())

def bfs(x):
    dq = deque([x])
    visit[x] = 1
    cnt = 0

    while dq:
        dq.popleft()

        for i in range(1,n+1):
            if visit[i] == 0:
                dq.append(i)
                visit[i] = 1
                cnt+=1
    return cnt


for _ in range(t):
    n,m = map(int,stdin.readline().rstrip().split())
    land = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,stdin.readline().rstrip().split())
        land[b][a] = 1

    visit = [0] * (n+1)
    
    print(bfs(1))



'''
먼저 0,1로 만들어진 그래프를 만든다
land = [[0]*(n+1) for _ in range(n+1)]로 0으로 가득찬 그래프 생성
for _ in range(m):
        a,b = map(int,stdin.readline().rstrip().split())
        land[b][a] = 1
이걸로 a,b쌍으로 나온 것을 1로 변환!
0만 있는 빈칸 생성 : visit = [0] * (n+1)
이전과 다른점은 visit를 한 줄로 만들어 한 줄 한 줄 비교한다는 점


'''