#AC - 자료구조

from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())
ans = []

for _ in range(t):
    p = sys.stdin.readline().rstrip() #글자
    n = int(sys.stdin.readline().rstrip()) #숫자
    x = deque(sys.stdin.readline().rstrip()[1:-1].split(',')) #배열
    r = 0
    d_list = deque()

    for i in range(len(p)):
        if len(x) == 0 or x[0]=='' and p[i] == 'D':
            ans.append('error')
            break
        elif p[i] == 'R':
            r+=1
            #reverse쓰면 안될듯
            #R의 개수를 세어 짝수 -> 왼쪽부터 삭제, 그냥 그대로 출력
            #홀수면 오른쪽 부터 삭제, 오른쪽부터 출력
        elif p[i] == 'D':
                if r%2 == 1:
                    x.pop()
                else:
                    x.popleft()
        if i == len(p)-1:
            if r%2 == 1:
                while len(x) != 0:
                    d_list.append(x.pop())
                ans.append('['+','.join(d_list)+']')
            else:
                while len(x) != 0:
                    d_list.append(x.popleft())
                ans.append('['+','.join(d_list)+']')
            
print(*ans,sep='\n')
