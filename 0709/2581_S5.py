#소수 - 기초수학2
import math

def sosu(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True


m = int(input())
n = int(input())
list = []
ans = []
for i in range(m,n+1):
    list.append(i)

for k in range(len(list)):
    if sosu(int(list[k])):
        ans.append(int(list[k]))

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))