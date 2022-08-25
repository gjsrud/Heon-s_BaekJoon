#듣보잡 - 집합,맵
#이분탐색
#from sys import stdin

#input = stdin.readline

#듣보잡 n
n,m = map(int,input().split())

no_hear = set()
no_see = set()


for _ in range(n):
    no_hear.add(input())
for _ in range(m):
    no_see.add(input())

'''
일단 sorted 함수는 정렬된 새로운 리스트를 리턴시켜줍니다. 
sort 메소드는 아무것도 리턴시켜주지 않습니다(None을 리턴) 
'''

dbj = sorted(list(no_see&no_hear))

print(len(dbj))
print(*dbj,sep='\n')
