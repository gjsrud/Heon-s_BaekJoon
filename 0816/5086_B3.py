#배수와 약수

ans = []

while True:
    a,b = map(int,input().split())
    if a == b == 0:
        print(*ans,sep='\n')
        break
    if a < b:
        if b%a == 0:
            ans.append('factor')
        else:
            ans.append('neither')
    elif a>b:
        if a%b == 0:
            ans.append('multiple')
        else:
            ans.append('neither')

