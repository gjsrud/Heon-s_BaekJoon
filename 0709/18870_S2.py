# 좌표 압축 - 정렬

n = int(input())
dic = {}

num = list(map(int,input().split()))
snum = sorted(set(num))

for i in range(len(snum)):
    dic[snum[i]] = i

for k in num:
    print(dic[k], end= ' ')
