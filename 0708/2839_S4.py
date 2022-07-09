#설탕배달 - 기본수학1


n = int(input())
cnt = 0

while n >= 0 :
    if n%5==0:
        cnt+=n//5
        print(cnt)
        break
        
    n-=3
    cnt+=1

else: #while이 거짓
    print(-1)
        