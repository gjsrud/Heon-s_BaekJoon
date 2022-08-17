#숨바꼭질 - 그래프 이론

from sys import stdin
from collections import deque
input = stdin.readline

def BFS(n):
    dq = deque([n])
    while dq:
        a = dq.popleft()
        if a == k:
            print(visit[a])
            break
        for i in (a-1,a+1,2*a):
            if not visit[i] and 0<= i <=100000:
                visit[i] = visit[a]+1
                dq.append(i)

'''
i는 a-1,a+1,2*a중에 하나를 택하고 
visit[i]는 과정이 한 번 지날 때 마다 1을 더해준다.
여기서 과정은 직전의 i값에 a-1,a+1,a*2를 한번 씩 취해준 것을 말한다

ex) 입력값 : 5 17
첫번째 
5 -> 4,6,10
두번째 
4 -> 3,5,8
6 -> 5,7,12
10 -> 9,11,20
세번쨰
......

'''

n,k = map(int,input().rstrip().split())
visit = [0] * 200001

BFS(n)