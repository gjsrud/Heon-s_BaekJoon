#나머지 - 1차원 배열

ans = set([])

for _ in range(10):
    num = int(input())
    na = num%42
    ans.add(na)

print(len(ans))