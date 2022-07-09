#부녀회장이 될테야 - 기본수학1

t = int(input())
ans = []
for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호수
    peo = [i for i in range(1,n+1)] #0층

    for a in range(k):
        for b in range(1,n):
            peo[b] += peo[b-1]

    ans.append(peo[-1])

print(*ans,sep='\n')
