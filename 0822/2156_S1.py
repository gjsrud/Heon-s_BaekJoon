# 포도주 시식 - 다이나믹 프로그래밍

from sys import stdin
input = stdin.readline

n = int(input())

dp = [0]*n
grape = []

for _ in range(n):
    grape.append(int(input()))

if n == 1:
    print(grape[0])
else:
    dp[0] = grape[0]
    dp[1] = dp[0] + grape[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3] + grape[i-1] + grape[i],dp[i-2] + grape[i],dp[i-1])
    print(dp[n-1])

'''
n이 6일 떄
6 10 13 9 8 1
dp[n]은 n번쨰의 최대값

n = 1일 때는 dp[0] = 6
n = 2일 때는 dp[1] = 16
n = 3일 때,
n[0] + n[2] = 19
n[1] + n[2] = 23 win!
dp[2] = 23
n = 4,
n[1] + n[3] = 19
n[0] + n[1] + n[3] = 25 == dp[1] + n[3]
n[0] + n[2] + n[3] = 28 
n = 5,
n[0] + n[1] + n[3] + n[4] = 33
n[0] + n[2] + n[4] = 27
n[1] + n[2] + n[4] = 31
n이 6일때,
1) 6을 마실 수 있어
    - 5를 마신경우 -> 4를 넘긴거 -> dp[2]+n[4]+n[5]
    - 5를 넘긴경우 -> dp[3]+n[5]
2) 6을 못마셔
    - 5를 마셨겠지 -> 4를 마셨다 -> 3은 넘김 -> dp[1]+n[3]+n[4] == dp[5]
    

즉, 3가지 중 가장 큰 수를 넣어야한다
1) dp[n-3] + grape[n-1] + grape[n]
2) dp[n-2] + grape[n]
3) dp[n-1]
'''