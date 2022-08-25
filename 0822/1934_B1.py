# 최소 공배수 - 조합론, 정수론
# 최소 공배수 = a*b/최대공약수

t = int(input())
ans = []

# 최대공약수 구하기(유클리드 호제법)
def yak(a,b):
    while b>0:
        temp = a
        a = b
        b = temp%b
    return a

for i in range(t):
    a,b = map(int,input().split())
    ans.append(int(a*b/yak(a,b)))

print(*ans,sep='\n')