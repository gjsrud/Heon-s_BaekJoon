#홀수

hol = []

for _ in range(7):
    a = int(input())
    if a%2 == 1:
        hol.append(a)

if len(hol) == 0:
    print(-1)
else:
    print(sum(hol))
    print(min(hol))