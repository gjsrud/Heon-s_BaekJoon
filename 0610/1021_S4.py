#회전하는 큐

from collections import deque

n,m = map(int,input().split())
list = list(map(int,input().split()))
dq = deque([i for i in range(1, n + 1)])

ans = []

while True:
    if len(dq) == n-m:
        break
    for k in list:
        if dq.index(k) < len(dq)/2:
            move = 0
            while True:
                if dq[0] == k:
                    dq.popleft()
                    ans.append(move)
                    break
                else:
                    dq.rotate(-1)
                    #print('<',dq,move+1)
                    move += 1
        else:
            move = 0
            while True:
                if dq[0] == k:
                    dq.popleft()
                    ans.append(move)
                    break
                else:
                    dq.rotate(1)
                    #print('>',dq,move+1)
                    move += 1


print(sum(ans))