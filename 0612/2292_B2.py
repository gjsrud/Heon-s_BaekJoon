n = int(input())

count = 1 
ans = 2 #거치는 방 개수

while True:
    last = 6*count+1
    if n == 1:
        print(1)
        break
    elif n <= last:
        print(ans)
        break
    else:
        count+=ans
        ans+=1