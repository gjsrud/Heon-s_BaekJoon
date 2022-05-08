a = int(input())
count = 0
b = []

for _ in range(a):
    jum = list(map(int,input().split()))
    s = sum(jum) - jum[0]
    v = s / jum[0]
    jum_one = jum[1:]
    count = 0
    for i in jum_one:
        if i > v:
            count += 1
            answer = count / jum[0] * 100
        else:
            answer = count / jum[0] * 100
    b.append(answer)


for i in range(len(b)):
    print("{:.3f}%".format(b[i]))
