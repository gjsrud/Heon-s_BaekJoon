#한수 - 함수
#브루트포스 알고리즘

n = int(input())

def BFa(n):
    cnt = 0
    for i in range(n+1):
        i = str(i)
        if i == '0' or i=='1000':
            pass
        else:
            k=len(i)
            if k==1:
               cnt+=1
            elif k==2:
                cnt+=1
            else:
                if int(i[1])-int(i[0]) == int(i[2])-int(i[1]):
                    cnt+=1
        
    return print(cnt)

BFa(n)



