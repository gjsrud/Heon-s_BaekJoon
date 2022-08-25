#최대공약수와 최소공배수 - 조합론,정수론

a,b = map(int,input().split())

#유클리드 호제법 - 최대공약수
def yak(a,b):
    while b>0:
        temp = a
        a = b
        b = temp%b
    return a

#유클리드 호제법 - 최소공배수
#최소공배수 = a*b/최대공약수
def bae(a,b):
    
    k = int(a*b/yak(a,b))
    return print(k)

print(yak(a,b))
bae(a,b)