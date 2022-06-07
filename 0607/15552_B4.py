import sys

t = int(sys.stdin.readline())
ans = []

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    p = str(a+b)
    ans.append(p)

print("\n".join(ans))