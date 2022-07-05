from collections import deque

a,b = map(str,input().split())
cnt = 1
flag = True

def BFS(b,a,cnt):
    dq = deque()
    dq.append(b)

    while dq:
        x = str(dq.popleft())
        if x[-1] == '1':
            x = x[:-1]
            cnt+=1
        elif int(x)%2 == 0:
            x = int(x)/2
            cnt+=1
        elif x[-1] != '1' and int(x)%2 == 1 or x==1:
            return -1

        x = int(x)
        
        if x == int(a):
            return cnt 
        elif x != int(a) and x!=1:
            dq.append(x)
        elif str(x)[-1] != '1' and x%2 == 1 or x==1:
            return -1
        

print(BFS(b,a,cnt))