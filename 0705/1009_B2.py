#분산처리

t = int(input())
ans = []

for _ in range(t):
    a,b = map(int,input().split())
    if a % 10 == 0:
        ans.append(10)
    else:
        a = a % 10
        if a in [1,5,6]:
            ans.append(a)
        elif a in [4,9]:
            #b%2가 짝수면 
            ans.append((a ** (b%2+2)%10))
        else:
            ans.append((a ** (b%4+4)%10))

print(*ans,sep='\n')

'''
1 = [1]
2 = [4,8,6,2]
3 = [9,7,1,3]
4 = [6,4]
5 = [5]
6 = [6]
7 = [9,3,1,7]
8 = [4,2,6,8]
9 = [1,9]

b가 8일때 --> 6 == a[3]
2 4 8 16 32 64 128 256 512 1024

2부터
6 4 6 4 6 4 6 4 6

'''