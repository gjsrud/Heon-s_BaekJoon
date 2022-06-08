ans = []
sign = {'(',')','[',']'}

while True:
    a = list(input())
    if len(a) == 1 and a[0] == '.':
        break
    elif len(a) != 1 and a[-1] == '.':
        s_list = []
        for k in range(len(a)):
            if a[k] in sign:
                s_list.append(a[k])
        i=0
        while True:
            i+=1
            if len(s_list)>1 and s_list[i-1:i+1] == ['(',')'] or s_list[i-1:i+1] == ['[',']']:
                del s_list[i-1:i+1]
                i=0
                continue
            elif i > 1 and len(s_list)==0:
                ans.append('yes')
                i=0
                break
            elif i > len(a):
                ans.append('no')
                i=0
                break

print('\n'.join(ans))


'''
So when I die (the [first] I will see in (heaven) is a score list).
stack ([]())
'''

'''
[(의 인덱스보다 )]의 인덱스가 빠를 수는 없다.
만약 [의 인덱스가 (의 인덱스 보다 작다면 ]는 )보다 인덱스 값이 커야한다.

'''