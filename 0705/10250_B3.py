#ACM호텔 - 기초수학1

cus = int(input())
ans = []

for _ in range(cus):

    floor = 1
    h,w,n = map(int,input().split())
    if n%h == 0:
        num = h
        floor = n//h
    else : 
        num = n%h
        floor += n//h

    if floor < 10:
        ans.append(str(num)+'0'+str(floor))
    else:
        ans.append(str(num)+str(floor))

print(*ans,sep='\n')


'''
num은 n%6
floor는 0에 몫을 더하면 나옴

2
20 20 180
010
ans : 2009
30 30 270
010
ans : 3009



'''