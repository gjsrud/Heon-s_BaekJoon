#파도반 수열

n = int(input())
ans = []

dp = [0]*101

dp[0] = 0
dp[1] = dp[2] = dp[3] = 1
dp[4] = 2


for _ in range(n):
    k = int(input())
    if k>5:
        for i in range(5,k+1):
            dp[i] = dp[i-5]+dp[i-1]
    ans.append(dp[k])

print(*ans,sep='\n')


'''
번호 길이 - 어떤 번호를 더한 값인가?
1	1 - 0
2	1 - 0,1
3	1 - 0,2
4	2 - 1,3

5	2 - 0,4
6	3 - 1,5
7	4 - 2,6
8	5 - 3,7
9	7 - 4,8
10	9 - 5,9
11	12 - 6,10
'''
