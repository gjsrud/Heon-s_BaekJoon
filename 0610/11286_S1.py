#절댓값 힙

import sys
import heapq

n = int(sys.stdin.readline())

q = []
mq = []
ans = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x>0:
        heapq.heappush(q,x)
    elif x<0:
        heapq.heappush(mq, -x)        
    else:
        if len(q) == len(mq) == 0:
            ans.append('0')
        elif len(q) == 0:
            ans.append(str(-heapq.heappop(mq)))
        elif len(mq) ==0:
            ans.append(str(heapq.heappop(q)))
        elif abs(q[0]) < abs(mq[0]):
            ans.append(str(heapq.heappop(q)))
        elif abs(q[0]) > abs(mq[0]):
            ans.append(str(-heapq.heappop(mq)))
        else:
            ans.append(str(-heapq.heappop(mq)))

print('\n'.join(ans))