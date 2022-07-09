#소인수분해 - 기본 수학2

n = int(input())

def soin(n):
    d = 2

    while d <= n:
        if n % d ==0:
            print(d)
            n =n/d
        else:
            d = d+1

soin(n)

