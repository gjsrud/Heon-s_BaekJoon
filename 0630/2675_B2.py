#문자열 반복

t = int(input())

for _ in range(t):
    ans = []

    a,b = map(str,input().split())
    for i in range(len(b)):
        ans.append(int(a)*b[i])

    print( ''.join(ans))

