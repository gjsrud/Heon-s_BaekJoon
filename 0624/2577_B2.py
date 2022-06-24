list = []

for _ in range(3):
    a = int(input())
    list.append(a)

num = str(list[0]*list[1]*list[2])


for i in range(10):
    cnt = 0

    for k in range(len(num)):
        #print(num[k],i)
        if num[k] == str(i):
            cnt += 1

    print(cnt)

