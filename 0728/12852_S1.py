#1로 만들기 2 - 그래프이론

from collections import deque

def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    
    while dq:
        a,b = dq.popleft()
        for n in [a+1,a*2,a*3]:
            if n <= num and check[n] == 0:
                if n == num:
                    return check[a]+1,b+[n]
                dq.append((n,b+[n]))
                check[n] = check[a]+1

num = int(input())
if num == 1:
    print(0)
    print(1)
else:
    check = [0]*(num+1)
    cnt,b = BFS(1,[1])
    print(cnt)
    print(*b[::-1])