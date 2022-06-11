from collections import deque

dq = deque()
n = int(input())
ans = []

for _ in range(n):
    x = int(input())
    if len(dq) == 0:
        dq.append(x)
    elif x < 0 and abs(x)<=(abs(min(dq))):
        dq.appendleft(x)
        print(dq)
    elif x > 0 and abs(x)<=(abs(min(dq))):
        dq.append(x)
        print(dq)
    elif x == 0:
        if dq[0] == dq[-1]:
            ans.append(str(dq.popleft))
        elif abs(dq[0]) < abs(dq[-1]):
            ans.append(str(dq.popleft))
        elif abs(dq[0]) > abs(dq[-1]):
            ans.append(str(dq.pop))
        elif len(dq) == 0:
            ans.append('0')

print('\n'.join(ans))

