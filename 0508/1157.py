a = list(input())

word = [x.lower() for x in a]

#print(word)

#for문과 try,except를 통해 counter라는 딕셔너리에 key:value형태로 넣어준다.
counter = {}
for value in word:
    try: counter[value] += 1
    except: counter[value] = 1

#일반 max로 나타내면 동률일 때 key값이 하나만 나온다.
#그래서 list comprehension을 사용하여 여러 개가 나올 수 있도록 한다.
b = [k for k,v in counter.items() if max(counter.values()) == v]


if len(b) > 1:
    print('?')
else:
    print(b[0].upper())



'''
list comprehension 문법
가장 기본적인 형태 : [expression for element in iterable]
조건문이 추가된 형태 : [expression for element in iterable if condition]
'''

