# 이항 계수 2 - 다이나믹 프로그래밍

n,k = map(int,input().split())

'''
nCk = n(n-1)(n-2)...(n-k+1) / k! 활용
'''

result = 1

for i in range(k):
    result *= n
    n -= 1

divisor = 1

for i in range(2,k+1):
    divisor *= i

print((result//divisor)%10007)