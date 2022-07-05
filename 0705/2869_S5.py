#달팽이는 올라가고 싶다 - 기초수학1
#(v-a) 에 (a-b) 로 며칠이 걸려야 도달할 수 있을까? 
import math
a,b,v = map(int,input().split())

up = a-b
    
day = math.ceil((v-a)/(up))
na = (v-a)%(up)


if a>=v:
    print(1)
else:
    day+=1
    print(day)


'''
v-a까지 도착
a만큼 더 가야 v까지 도착

2 1 5 -> 3에 1이 도달 : 3일이면 도착
5 1 6 -> 1에 4가 도달 : 1일이면 도착
7 4 12 -> 5에 3이 도달 : 2일 도착
'''