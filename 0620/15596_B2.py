#정수 N개의 합 - 함수정의

def solve(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    return sum