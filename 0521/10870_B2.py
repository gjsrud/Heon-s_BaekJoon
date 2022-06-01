#피보나치 수열

n = int(input())
pibo = [0,1]
ans = 0

'''
피보나치
0 1 1 2 '3' 5 8 13 21 34....
1 2번째는 정해져 있다
n이 5이다
반복 -> n[3]
'''

for i in range(n):
    if i==0:
        pibo.append(1)
    else:
        ans = pibo[i]+pibo[i+1]
        pibo.append(ans)

print(pibo[-2])