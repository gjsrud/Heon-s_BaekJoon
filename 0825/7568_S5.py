# 덩치 - 브루트 포스

n = int(input())
dong = []
ans = []
for i in range(n):
    x = list(map(int,input().split()))
    dong.append(x)

for i in range(n):
    num = 1
    for k in range(n):
        if i != k:
            if dong[i][0] < dong[k][0] and dong[i][1] < dong[k][1]:
                num+=1
    ans.append(num)

print(*ans,sep=' ')

'''
11 22
11 33
11 44
11 55
22 11
22 33
'''