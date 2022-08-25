# 분해합 - 브루트포스

N = int(input())
result = 0

for i in range(1, N + 1):
  tmp = i + sum(map(int,str(i)))

  if tmp == N:
    result = i
    break

print(result)




'''
314675
첫자리는 2
둘쨰자리 0~9

'''