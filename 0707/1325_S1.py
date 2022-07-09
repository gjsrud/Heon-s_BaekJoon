#효율적인 해킹 - 그래프 이론

from collections import deque
from sys import stdin


def BFS(x):
    visit = [False]*(n+1)
    dq = deque([x])
    visit[x] = True
    cnt = 1
    while dq:
        a=dq.popleft()
        for i in gra[a]:
            #if not은 결과가 거짓이면 실행
            # 0, [], {}, '', 빈세트 등이 False로 이해됨
            if not visit[i]:
                dq.append(i)
                #print(dq)
                
                visit[i] = True
                cnt+=1
    return cnt


#n - 컴퓨터 개수 , m - 관계 수
n,m = map(int,stdin.readline().rstrip().split())
list_m = [0]
ans = []
gra = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = list(map(int,stdin.readline().rstrip().split()))
    gra[y].append(x)

result = []
for i in range(1, n+1):
    result.append(BFS(i))

max = max(result)
for i in range(len(result)):
    if max == result[i]:
        print(i+1, end=' ')

'''
for i in range(1,n+1):
    if BFS(i)>max(list_m):
        ans = []
        ans.append(i)
        list_m = []
        list_m.append(BFS(i))        
    elif BFS(i)==max(list_m):
        ans.append(i)
    else:
        pass

print(*ans,sep=' ')
'''