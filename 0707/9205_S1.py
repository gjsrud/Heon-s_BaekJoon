#맥주 마시면서 걸어가기 - 그래프 이론

from collections import deque

'''
dx,dy가 아니었음. 한번씩 갈 필요없이 노드 간 거리가 1000이상이면 실패임
'''

t = int(input())
ans = []

def BFS():
    dq = deque()
    dq.append([home[0],home[1]])
    
    while dq:
        a,b = dq.popleft()
        if abs(a-end[0]) + abs(b-end[1]) <= 1000:
            ans.append('happy')
            return 
        for i in range(n):
            if not visit[i]:
                store_x,store_y = store[i]
                if abs(a-store_x)+abs(b-store_y) <= 1000:
                    dq.append([store_x,store_y])
                    visit[i] = 1             
    ans.append('sad')
    return 
    

           
for _ in range(t):
    n = int(input())
    home = list(map(int,input().split()))
    store = []
    for _ in range(n):
        x,y = map(int,input().split())
        store.append([x,y])
    end = list(map(int,input().split()))
    visit = [0 for _ in range(n+1)]
    BFS()


print(*ans,sep='\n')