a = int(input())
count = 0
b = []

for _ in range(a):
    jum = list(map(int,input().split())) #점수
    s = sum(jum) - jum[0] #점수 다  더하고 1번째 빼줌
    v = s / jum[0] #평균
    jum_one = jum[1:] #2번째 부터 전부
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
