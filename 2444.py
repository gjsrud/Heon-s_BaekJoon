n = int(input())

for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))

for a in range(n-1,0,-1):
    print(' '*(n-a)+'*'*(2*a-1))
