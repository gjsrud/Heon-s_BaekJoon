# 제곱수의 합 - 다이나믹 프로그래밍

from sys import stdin
input = stdin.readline

n = int(input())
dp = [x for x in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])


'''
dp값을 1부터 n까지 하나씩 갱신해가는 방법.
i로 1부터 n까지 돌면서, j는 1부터 i-1까지의 수 중 제곱한 값이 i보다 크지 않아야 한다.
즉, 예를 들어 dp[6] = dp[6 - 2*2] + 1 = dp[2] + 1이다. 
    여기서 1을 더해 주는 이유는 2*2 의 경우를 더한 것이기 때문이다.
'''

