#소트인사이드 - 정렬

n = input()

ans = []
num = 0

for i in range(len(n)):
    ans.append(n[i])

ans.sort(reverse=True)

print(*ans,sep='')