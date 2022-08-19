# 1로 만들기 - 다이나믹 프로그래밍
n = int(input())

dp = [0] * (n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1]+1   #1 뺏을 때
    if i%3==0: dp[i] = min(dp[i],dp[i//3]+1)    #3으로 나눌 때
    if i%2==0: dp[i] = min(dp[i],dp[i//2]+1)    #2로 나눌 때

print(dp[n])

'''
dp는 만들 수 있는 최솟값을 저장 -> 중요
위의 식에서 +1은 값을 더하는게 아니고 순서가 한 턴 지났음을 의미
'''