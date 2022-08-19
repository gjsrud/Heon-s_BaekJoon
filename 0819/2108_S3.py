# 통계학 - 정렬

from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
num = []

for _ in range(n):
    a = int(input())
    num.append(a)
    
#산술평균
print(round(sum(num)/n))

#중앙값
num.sort()
print(num[n//2])

#최빈값

cnt_num = Counter(num).most_common()
if len(cnt_num) > 1 and cnt_num[0][1] == cnt_num[1][1]:
    print(cnt_num[1][0])
else:
    print(cnt_num[0][0])
    

#범위
print(max(num)-min(num))


'''
Counter(num).most_common()
사용하면 [(숫자,개수)] 형태로 나온다
여기서 개수가 많은 숫자 우선, 숫자는 오름 차순 정렬!
ex) [9,9,9,1,1,4,4,5]라면 [(9, 3), (1, 2), (4, 2), (5, 1)]과 같은 형태
'''