# DFS와 BFS - 그래프이론

from collections import deque,defaultdict
from sys import stdin

# 참고 : https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
# 반례 모음 : https://www.acmicpc.net/board/view/24356
'''
    dfs : 한 노드의 자식 노드까지 다 찍고 오기
    bfs : 같은 깊이의 노드를 다 탐색 후 다음 깊이의 노드 탐색

'''

n,m,v = map(int,stdin.readline().split())
gra = defaultdict(list)



for _ in range(m):#그래프 완성
    a, b = map(int, stdin.readline().split())
    gra[a].append(b)
    gra[b].append(a)

for i in gra:
    gra[i].sort()

#print(gra)

def DFS(graph, root):
    visit = []
    stack = [root]
    
    while stack:
        n= stack.pop() #깊이 들어가기
        if n not in visit:
            visit.append(n)
            a=list(set(graph[n])-set(visit))
            a.sort(reverse=True)
            stack+=a
    return visit


def BFS(graph, root):
    visit=[]
    dq=deque([root])

    while dq:
        n = dq.popleft()
        if n not in visit:
            visit.append(n)
            a = list(set(graph[n])-set(visit))
            a.sort()
            dq+=a
            
    return visit

print(*DFS(gra,v),sep=' ')
print(*BFS(gra,v),sep=' ')
'''
BFS예제
5 5 3
5 4
5 2
1 2
3 4
3 1

dq는 [3]
n은 3, dq는 []
visit [3]
dq+=graph[n]-set(visit)
--> [] += {1,4}-{3}
dq == ([1,4])

n은 1, dq는 [4]
visit [3,1]
dq+=graph[n]-set(visit)
--> [4] += {2,3}-{3}
dq == [4,2]

...


'''