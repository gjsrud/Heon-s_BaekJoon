from re import X


ans = []
t = int(input())

'''
원으로 봐야한다! 두 원이 겹치는 곳이 류재명이 있을 수 있는 범위로 보겠음
두 원의 거리를 구해서 그 거리가 내접,외접하면 한 점에서 만나는 것
교차한다면 두 점에서 만나는 것
중심과 반지름이 같으면 무한대 (-1)
외부에 있거나 작은원이 안에 있는데 마주치지 않거나 두 원의 중심은 같은데 반지름이 다른경우 0

두 원 사이의 거리 ((x1-x2)**2+(y1-y2)**2)**0.5

'''

for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    if x1==x2 and y1==y2 and r1==r2:
        ans.append('-1')
    elif r1+r2 > d and abs(r1-r2)<d:
        ans.append('2')
    elif r1+r2 == d or abs(r1-r2) == d:
        ans.append('1')
    elif r1+r2 < d or abs(r1-r2) > d:
        ans.append('0')

print('\n'.join(ans))
