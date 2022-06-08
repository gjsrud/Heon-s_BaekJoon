# 최대 힙

import sys
import heapq

n = int(sys.stdin.readline())
que = []
ans = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x>0:
        heapq.heappush(que,(-x,x))
    else:
        if len(que) == 0:
            ans.append('0')
        else:
            ans.append(str(heapq.heappop(que)[1]))

print("\n".join(ans))