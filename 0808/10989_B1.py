from sys import stdin

input = stdin.readline

n = int(input())
ans=[0 for _ in range(10001)] #수를 세어줄 배열


# 인풋으로 받은 수가 몇변 들어왔는지 빈도 저장
for _ in range(n):
    a = int(input())
    ans[a] += 1

for i in range(1,10001):
    count = ans[i]
    for _ in range(count):
        print(i)