# 블랙잭 - 브루트 포스

n,m = map(int,input().split())

ans = list(map(int,input().split()))
max = 0

for i in range(len(ans)):
    for k in range(i+1,len(ans)):
        for q in range(k+1,len(ans)):
            diff = ans[i]+ans[k]+ans[q]
            if diff <= m and diff > max:
                max = diff

print(max)

'''
123
124
125
134
135
145
'''