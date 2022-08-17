#합분해 - 다이나믹 프로그래밍

from sys import stdin

input = stdin.readline().rstrip

#n은 합이 되는 수 / k는 더하는 개수
n,k = map(int,input().split())

dp = [[0]*201 for _ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i +1

for i in range(2,201):
    dp[i][1] = i
    for h in range(2,201):
        dp[i][h] = (dp[i][h-1]+dp[i-1][h])%1000000000

print(dp[k][n])