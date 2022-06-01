import math

ans = []

n,w,h = map(int,input().split())
x = math.sqrt(w**2+h**2)

for _ in range(n):
    a = int(input())
    if a <= x:
        ans.append('DA')
    else:
        ans.append('NE')

print('\n'.join(ans))