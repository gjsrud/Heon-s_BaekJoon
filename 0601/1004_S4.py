import sys

'''
두 점 다 원 안에 있으면 print(0)
둘 다 원 밖에 있으면 0
둘 중 하나만 원 안에 있으면 +1

x1,y1과 cx,cy의 거리가 r보다 크면 원 밖에 있는거
'''

ans = []

t = int(sys.stdin.readline())

for i in range(t):
    ans_count = 0
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for _ in range(n):
        cx,cy,r = map(int,sys.stdin.readline().split())
        d1 = ((x1-cx)**2+(y1-cy)**2)**0.5
        d2 = ((x2-cx)**2+(y2-cy)**2)**0.5
        if d1 < r and d2 < r:
            ans_count == 0
        elif d1 > r and d2 <r or d1 < r and d2 >r:
            ans_count += 1
        elif d1 > r and d2 > r:
            ans_count += 0
    ans.append(str(ans_count))

print('\n'.join(ans))