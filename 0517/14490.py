import math

a,b = map(int,input().split(':'))

n = math.gcd(a,b)

a_n = int(a/n)
b_n = int(b/n)

print('%d:%d' % (a_n,b_n))