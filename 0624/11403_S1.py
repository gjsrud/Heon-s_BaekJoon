#미로탐색

n = int(input())

gra = []
visit = [0 for _ in range(n)]

for _ in range(n):
    a = list(map(int, input().split()))
    gra.append(a)
    #visit.append(b)


def WP(x):
    for i in range(n):
        if gra[x][i] == 1 and visit[i] == 0:
            visit[i] = 1
            WP(i) #이걸 적어주는게 그 노드도 연결 되어있으면 1로 바꿔줘야하기 떄문에

for i in range(n):
    WP(i)
    for k in range(n):
        if visit[k]==1:
            print(1,end=" ")
        else:
            print(0,end = " ")
    print()
    visit = [0 for _ in range(n)]

'''
0 1 0
0 0 1
1 0 0

WP(0)
처음 걸리는게 [0][1]
visit [0,1,0]으로 변경
->WP(1)
gra[1][2]이 걸림
visit [0,1,1]
->WP(2)
gra[2][1]이 걸림
visit [1,1,1]
visit가 0이 없어 if문을 만족시키지 못하므로 WP(0)이 종료

'''