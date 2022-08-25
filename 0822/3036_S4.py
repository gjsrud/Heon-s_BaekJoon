# 링 - 정수론, 조합론

n = int(input())
ring = list(map(int,input().split()))
ans = []

# 최대공약수
def yak(a,b):
    while b>0:
        temp = a
        a = b
        b = temp%b
    return a

for i in range(1,len(ring)):
    num = yak(ring[0],ring[i])
    print(f'{int(ring[0]/num)}/{int(ring[i]/num)}')

