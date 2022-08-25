#검문 - 조합론, 정수론

from sys import stdin
input = stdin.readline

#최대공약수
def yak(a,b):
    while b>0:
        temp = a
        a = b
        b = temp%b
    return a

n = int(input())
num = []
ans = []


for _ in range(n):
    m = int(input())
    num.append(m)

num.sort()

for i in range(len(num)):
    if i+1 <= len(num)-1:
        ans.append(num[i+1]-num[i])

GCD = ans[0]

for i in range(1,len(ans)):
    GCD = yak(GCD,ans[i])

result = set()

for i in range(2,int(GCD**0.5)+1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)

result = list(result)
result.sort()

print(*result)
