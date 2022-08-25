# 약수 - 정수론, 조합론

n = int(input())

yak = list(map(int,input().split()))

ans = max(yak) * min(yak)

print(ans)