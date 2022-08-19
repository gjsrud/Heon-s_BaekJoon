#영수증 - 반복문

x = int(input())
n = int(input())
p = 0

for _ in range(n):
    a,b = map(int,input().split())
    p+=a*b

if p==x:
    print('Yes')
else:
    print('No')