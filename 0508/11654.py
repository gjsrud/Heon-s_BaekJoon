import sys

print(ord(sys.stdin.readline().rstrip()))

'''
ord() : 특정한 한 문자를 아스키 코드 값으로 변환해주는 함수
sys.stdin.readline() : 반복문으로 여러줄 입력받을 때 쓰면 시간 초과가 발생하지 않는다
   개행문자 또한 저장하므로 A를 입력하면 A\로 입력된다. 그래서 사용한게 rstrip
rstrip : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
참고 : https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readlinehttps://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline
'''