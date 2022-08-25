# 가장 긴 증가하는 부분 수열 - 다이나믹 프로그래밍

from sys import stdin
input = stdin.readline().rstrip

n = int(input())

for i in range(n):
    li = list(map(int,input().split()))

dp = [1]*n

for i in range(n):
    for k in range(i):
        if li[i] > li[k]:
            dp[i] = max(dp[i],dp[k]+1)

print(max(dp))


'''
1. dp[i]의 값을 1로 초기화
2. 현재 위치(i)보다 이전에 있는 원소(k)가 작은지 확인한다. (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)
3. 작다면, 현재 위치의 이전 숫자(dp[k]) 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.
'''