#소수 찾기 - 기초 수학2

import math

def sosu(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True

n = int(input())
list = list(input().split(' '))
cnt = 0

for i in range(len(list)):
    if sosu(int(list[i])):
        cnt+=1

print(cnt)
