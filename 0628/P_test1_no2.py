def solution(s):
    if s[0] == '+':
        s = int(s[1:])
    elif s[0] == '-':
        s = int(s)
    else:
        s = int(s)
    answer = print(s)
    return answer

solution('-1234')