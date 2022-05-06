h,m = map(int, input().split())
c = int(input())

hc = h+c//60
mc = m+c%60
if mc > 59:
    hc = hc+1
    mc = mc-60

if hc > 23:
    print(str(hc-24) + ' ' + str(mc))
else:
    print(str(hc) + ' ' + str(mc))