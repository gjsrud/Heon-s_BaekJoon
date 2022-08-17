#베르트랑 공준 - 기초 수학 2
#에라토스테네스의 체 사용
'''
에라토스테네스의 체 알고리즘
2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
2부터 시작해서 나열된 수에서 지워지지 않은 수 중 가장 작은 2를 소수로 선택하고 2의 배수를 지운다.
3도 지워지지 않았기 때문에 소수로 선택하고 3의 배수를 지운다.
4는 지워졌기 때문에 넘어가고 5를 소수로 선택하고 5의 배수를 지운다.
2,3,4와 같은 과정을 반복한다.
반복이 끝나면 지워지지 않은 수들을 소수로 출력한다.
'''
import math
from sys import stdin

ans = []

#에라토스테네스의 체
def eratos(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    
    return True

while True:
    n = int(stdin.readline())

    if n == 0:
        break
    
    cnt = 0

    for i in range(n+1,(2*n)+1):
        if eratos(i):
            cnt += 1
    

    print(cnt)
    
