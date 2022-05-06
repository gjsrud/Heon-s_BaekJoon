h,m = map(int,input().split())

if m < 45:
    if h == 0:
        print(str(23) + " " + str(m+15))
    else:
        print(str(h-1) + " " + str(m+15))
else:
    print(str(h) + " " + str(m-45))
