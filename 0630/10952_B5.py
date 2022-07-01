#A+B - 5 - 반복문

ans = []

while True:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    else:
        ans.append(a+b)

print(*ans,sep="\n")