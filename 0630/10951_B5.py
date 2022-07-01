#A+B - 4 - 반복문

ans = []

while True:
    try:
        a,b = map(int,input().split())
        ans.append(a+b)
    except:
        break

print(*ans,sep="\n")