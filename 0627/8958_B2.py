n = int(input())

ans = []


for _ in range(n):
    l_sum = []
    que = list(input())
    cnt = 0
    for i in range(len(que)):
        if que[i] == 'O':
            cnt += 1
            l_sum.append(cnt)
        else:
            cnt = 0
            pass
    ans.append(sum(l_sum))

print(*ans,sep='\n')
