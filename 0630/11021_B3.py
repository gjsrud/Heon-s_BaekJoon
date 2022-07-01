#A+B - 7 - 반복문

t = int(input())
ans = []
for _ in range(t):
    a,b = map(int,input().split())
    ans.append(a+b)

for i in range(len(ans)):
    print(f'Case #{i+1}:', ans[i])