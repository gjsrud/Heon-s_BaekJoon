#큐

from collections import deque

n = int(input())
dq = deque()
ans = []


for _ in range(n):
    a = input()
    if a[:3] == 'pus':
        num = int(a[5:])
        dq.append(num)
    elif a == 'pop':
        if len(dq) == 0:
            ans.append(-1)
        else: 
            k = dq.popleft()
            ans.append(k)
    elif a == 'size':
        ans.append(len(dq))
    elif a == 'empty':
        if len(dq) == 0:
            ans.append(1)
        else:
            ans.append(0)
    elif a == 'front':
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq[0])
    elif a == 'back':
        if len(dq) == 0:
            ans.append(-1)
        else:
            ans.append(dq[-1])

print(*ans,sep="\n")