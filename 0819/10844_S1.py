# 쉬운 계단 수 - 다이나믹 프로그래밍

n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1): #i는 자리수
    for k in range(10):
        if k == 0:
            dp[i][k] = dp[i-1][1]
            print('0',dp[i][k])
        elif k == 9:
            dp[i][k] = dp[i-1][8]
            print('9',dp[i][k])
        else:
            dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]
            print(k,dp[i][k])
              
print(sum(dp[n])%1000000000)




'''

dp = [[]*10]
0부터 9까지 만들고
어차피 첫자리가 0인건 제외니까 0빼고 1~9까지 1을 넣어줘
-> n이 1일 때 만들 수 있는 계단 수
n이 2
k가 0일때는 
dp[2][0] = dp[1][1] == 1
dp[2][9] = dp[1][8] == 1

이거 참고
앞에 오는 숫자 = 0 )
dp[자리 수][0] = dp[자리 수 - 1][1]
※ dp[1][0] = 0이기 때문에 어차피 결과엔 영향을 미치지 않는다.
ex) 0, 01, 012 -> 안 셈!

앞에 오는 숫자 = 1~8 )
dp[자리 수][앞에 오는 숫자] = dp[자리 수 - 1][앞에 오는 숫자 -1] + dp[자리 수 - 1][앞에 오는 숫자 + 1]
dp[n][i] = dp[n][i-1] + dpㅈ

앞에 오는 숫자 =9 )
dp[자리 수][9] = dp[자리 수 - 1][8]
출처: https://cotak.tistory.com/12 [TaxFree:티스토리]
'''