t = int(input())
num=[]

for i in range(t):
    a,b = map(int,input().split())
    num.insert(i,a+b)

for y in range(t):
    print(num[y])