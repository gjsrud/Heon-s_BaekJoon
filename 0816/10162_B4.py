#전자레인지

t = int(input())
a = b = c = 0


while t > 0:
    if t%10 != 0:
        break
    if t >= 300:
        t -= 300
        a+=1
    elif t >= 60:
        t -= 60
        b+=1
    elif t >= 10:
        t -= 10
        c+=1

if a == b == c == 0:
    print(-1)
else:
    print(a,b,c)