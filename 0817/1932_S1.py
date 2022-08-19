#정수 삼각형 - 다이나믹 프로그래밍

n = int(input())
ans = [[0]*n for _ in range(n)]
tri = []
for i in range(n):
    tri.append(list(map(int,input().split())))

ans[0] = tri[0]

for i in range(1,n): #삼각형 줄
    for k in range(i+1): #ans 번호
        if k == 0:
            ans[i][k] = ans[i-1][0]+tri[i][k]
        elif i == k:
            ans[i][k] = ans[i-1][k-1]+tri[i][k]
        else:
            ans[i][k] = max(ans[i-1][k],ans[i-1][k-1])+tri[i][k]

print(max(ans[n-1]))
'''
7
3 8
8 1 0
2 7 4 4
i가 1
ans[1][0] = ans[0][0]+ tri[1][0]
ans[1][1] = ans[0][0]+ tri[1][1]
3번쨰 줄 봐바

ans[2][0] = max(ans[0][0],ans[0][-1])+tri[2][0]
ans[2][1] = max(ans[1][0],ans[1][1])+tri[2][1]
ans[2][2] = ans[1][1]+tri[2][2] 
4번째 줄
ans[3][0] = ans[0]+tri[3][0]
ans[3][1] = max(ans[2][0],ans[2][1])+tri[3][1]
ans[3][2] = max(ans[2][1],ans[2][2])+tri[3][2]
ans[3][3] = ans[2][2]+tri[3][3]

즉, 1과 마지막을 제외한 값은 
'''