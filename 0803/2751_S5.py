# 수 정렬하기 2 - 정렬
# 빠른 정렬 위해 merge sort 사용해보기

'''
merge sort
배열을 1개까지 모두 쪼갠 후 합치며
합칠 때 마다 오름 차순 정렬하는 방법

ex) [2,4,3,6,5,1]
[2,4] [3,6] [5,1]
[2] [4] [3] [6] [5] [1]
[2,4] [3,6] [1,5]
[2,3,4,6] [1,5]
[1,2,3,4,5,6]
'''

from sys import stdin
input = stdin.readline


n = int(input())
ans = []

for _ in range(n):
    num = int(input())
    ans.append(num)

#쪼개는 함수
def merge_sort(list):
    if len(list) <= 1:
        return list
    
    #리스트를 2분할
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    #분할한 리스트를 merge_sort함수를 이용하여 나누기
    left_temp = merge_sort(left)
    right_temp = merge_sort(right)
    return merge(left_temp, right_temp)

#다시 합치는 함수
def merge(left,right):
    i = k = 0
    sort_list = []
    while i < len(left) and k < len(right):
        if left[i] < right[i]:
            sort_list.append(left[i])
            i+=1
        else:
            sort_list.append(right[k])
            k += 1
    while i < len(left):
        sort_list.append(left[i])
        i+=1
    while k < len(right):
        sort_list.append(right[k])
        k+=1
    return sort_list        
        

print(*merge_sort(ans),sep='\n')