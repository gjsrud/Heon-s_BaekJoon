#수 정렬하기 - 정렬

n = int(input())
ans = []
for _ in range(n):
    x = int(input())
    ans.append(x)

ans.sort()

print(*ans,sep='\n')

