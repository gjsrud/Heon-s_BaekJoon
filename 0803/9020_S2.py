#골드바흐의 추측 - 기초 수학 2
# 소수 구하기 위해 에라토스테네스의 체 활용
# 두 소수의 합이 가장 작은 소수를 가져오라

'''
타겟이 되는 수의 반을 a,b로 잡고
a,b가 소수면 그대로 종료
a,b가 소수가 아니면 각각 +1,-1을 해줄 것
'''

import math
from sys import stdin
input = stdin.readline

def eratos(n):
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    
    return True

t = int(input())
ans = []

for _ in range(t):
    num = int(input())
    a = num//2
    b = num//2

    while True:
        if eratos(a) == True and eratos(b) == True:
            ans.append([a,b])
            break
        else:
            a-=1
            b+=1

for i in range(len(ans)):
    print(ans[i][0],ans[i][1])
    
    
    
