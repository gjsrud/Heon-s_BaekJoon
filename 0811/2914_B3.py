#저작권

a,i = map(int,input().split()) #곡 개수, 평균값

'''
멜로디 개수 / 곡 개수 = 올린 평균값
최소 멜로디 = (올린 평균값-1+0.01) * 곡 개수
'''
x = a * (i-1+0.01)

print(int(x)+1)