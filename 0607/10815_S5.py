import sys

n = int(sys.stdin.readline())
sang = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
gyo = set(sang)&set(card)

ans = []

for i in range(len(card)):
    if card[i] in gyo:
        ans.append(1)
    else:
        ans.append(0)


print(*ans)

