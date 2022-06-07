w,h,x,y,p = map(int,input().split())
count = 0

for _ in range(p):
    a,b = map(int,input().split())
    l_len = ((a-x)**2+(b-(y+h/2))**2)**0.5
    r_len = ((a-(x+w))**2+(b-(y+h/2))**2)**0.5
    if a >= x and b >= y and a <=(x+w) and b <= (y+h):
        count += 1
    elif l_len <= h/2 or r_len <= h/2:
        count += 1
    else:
        pass

print(count)