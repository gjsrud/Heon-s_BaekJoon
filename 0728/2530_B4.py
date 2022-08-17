#인공지능 시계

h,m,s = map(int,input().split())
cook = int(input())

cook_m = cook // 60

s += cook-(cook_m*60)
m += cook_m

while True:
    if s<60 and m<60 and h<24:
        break
    if s>59:
        a =s//60 
        m+=a
        s-=(a*60)
    elif m>59:
        b =m//60 
        h+=b
        m-=(b*60)
    elif h>23:
        c=h//24
        h-=c*24


print(h,m,s,sep=' ')
