#회전하는 큐 - 문제 이해 못함

from collections import deque

n,m = map(int,input().split())
list = list(map(int,input().split()))
dq = deque([i for i in range(1, n + 1)])

ans = []

while True:
    if len(dq) == n-m:
        break
    for k in range(len(list)):
        if list[k] <= (len(dq)+1)/2:
            move = 0
            while True:
                if dq[0] == list[k]:
                    dq.popleft()
                    dq.rotate(move)
                    ans.append(move)
                    break
                else:
                    dq.rotate(-1)
                    #print('<',dq,move+1)
                    move += 1
        else:
            move = 0
            while True:
                if dq[0] == list[k]:
                    dq.popleft()
                    dq.rotate(-(move-1))
                    ans.append(move)
                    break
                else:
                    dq.rotate(1)
                    #print('>',dq,move+1)
                    move += 1


print(sum(ans))