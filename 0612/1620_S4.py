#나는야 포켓몬 마스터
#딕셔너리 활용

import sys

n,m = map(int, sys.stdin.readline().split())

pika = {}

for k in range(1,n+1):
    #딕셔너리는 개행문자도 따라오기 때문에 rstrip으로 제거해줘야한다.
    y = sys.stdin.readline().rstrip() #rstrip() -> 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
    pika[y] = str(k)
    pika[str(k)] = y
    #이러면 모든 숫자와 글자가 key값으로 들어온다

for _ in range(m):
    print(pika[sys.stdin.readline().rstrip()])