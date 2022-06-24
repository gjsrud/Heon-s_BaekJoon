#바이러스 - 그래프이론

from collections import defaultdict,deque

com = int(input())
c = int(input())
start = 1
gra = defaultdict(list)

for _  in range(c):
    a,b = list(map(int,input().split()))
    gra[a].append(b)
    gra[b].append(a)


def BFS(graph, start):
    visit = []
    dq = deque([start])

    while dq:
        n = dq.popleft()
        if n not in visit:
            visit.append(n)
            a = list(set(graph[n])-set(visit))
            a.sort()
            dq+=a
    
    del visit[0]
    return len(visit)

print(BFS(gra,start))
