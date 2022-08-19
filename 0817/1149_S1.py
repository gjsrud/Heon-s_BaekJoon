#RGB거리 - 다이나믹 프로그래밍

n = int(input())
rgb = []
for i in range(n):
    c = list(map(int,input().split()))
    rgb.append(c)

for i in range(1,len(rgb)):
    #red
    rgb[i][0] = rgb[i][0] + min(rgb[i-1][1],rgb[i-1][2])
    #green
    rgb[i][1] = rgb[i][1] + min(rgb[i-1][0],rgb[i-1][2])
    #blue
    rgb[i][2] = rgb[i][2] + min(rgb[i-1][0],rgb[i-1][1])

print(min(rgb[n-1]))

'''
26 40 83
49 60 57
13 89 99
일 때
i = 1 - r:26    g:40    b:40
i = 2 - r:49+min(rgb[1][1],rgb[1][2])   g:60+min(rgb[1][0],rgb[1][2])   b:57+min(rgb[1][1],rgb[1][2])
즉, 현재 rgb에 들어있는 값 + 현재 선택한 색상을 제외한 두 색중에 앞집에 칠한 값이 적은 색 선택하여 더하기
red : rgb[i] = rgb[i]+min(rgb[n-1][1],rgb[n-1][2])

이제 3개의 집 즉, n-1번쨰 리스트의 가장 작은 값을 출력하면 된다
'''