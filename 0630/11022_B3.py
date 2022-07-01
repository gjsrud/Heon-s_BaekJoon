#A+B - 8 - 반복문

t = int(input())
ans = []
al = []
bl = []
for _ in range(t):
    a,b = map(int,input().split())
    ans.append(a+b)
    al.append(a)
    bl.append(b)

for i in range(len(ans)):
    print(f'Case #{i+1}:',al[i],'+',bl[i],'=',ans[i])