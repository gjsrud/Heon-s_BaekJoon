#연속합 - 다이나믹 프로그래밍

n = int(input())
num=list(map(int,input().split()))

dp = [0]*n
dp[0] = num[0]

for i in range(1,n):
    dp[i] = max(num[i],dp[i-1]+num[i])

print(max(dp))

'''
dp[i]는 max(num[i],dp[i-1]+num[i])
이렇게 쓰면
dp[i-1] ->  얘는 앞의 값을 더한 것 (num[n-1]해버리면 그냥 앞의 값만 더한 것)
거기다 dp[i]를 더하면 앞의 값들을 더해 온 것임
'''