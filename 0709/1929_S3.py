#소수 구하기 - 기본 수학2
import math

m,n = map(int,input().split())

ans = []

def sosu(x):
    if x == 1:
        return False
    for a in range(2,int(math.sqrt(x))+1):
        if x%a == 0:
            return False
    return True

for i in range(m,n+1):
    if sosu(i):
        ans.append(i)

print(*ans,sep='\n')
