import sys

n, m = map(int,sys.stdin.readline().split())
n_set = set()
m_list = []
ans = 0

for _ in range(n):
    a = input()
    n_set.add(a)
for _ in range(m):
    b = input()
    m_list.append(b)


for i in range(len(m_list)):
    if m_list[i] in n_set:
        ans+=1
    else:
        ans+=0

print(ans)