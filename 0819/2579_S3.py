#계단 오르기 - 다이나믹 프로그래밍

n = int(input())
dp = [0]*(n+1)
stairs = [0]*(n+1)

for i in range(1,n+1):
    stairs[i] = int(input())

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1]+stairs[2])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1]+stairs[2]
    dp[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])

    for k in range(4,n+1):
        dp[k] = max(stairs[k]+stairs[k-1]+dp[k-3],stairs[k]+dp[k-2])
    print(dp[-1])

    

'''
마지막(i)은 무조건 밟는다
그럼 마지막 전 계단은 두 가지 경우가 생김
1은 그대로 첫 계단 값
2는 1계단 + 2계단
3은 1,3계단, 2,3계단 중 큰 값
1. i-3을 밟고 i-2를 밟고 바로 i를 밟는 경우
2. i-2를 밟지 않고 i-1을 밟고 i를 밟는 경우

n번 째 계단을 구하기
dp(n) = max(직전 계단의 최댓값, 전전 계단의 최대값)
직전 계단의 최댓값 = 직전 계단 값(n-1) + n번째 계단 값 + 직전 계단의 두 칸 전 최대값(n-3)
    => 왜? 직전 계단에서는 한 칸 띄워야 하기 때문에 n-3의 최대 값을 구함


'''