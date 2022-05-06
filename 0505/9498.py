exam = int(input())

if exam < 0 or exam > 100:
    print('올바른 숫자를 입력하시오')
else:
    if exam >= 90:
        print('A')
    elif exam >= 80:
        print('B')
    elif exam >= 70:
        print('C')
    elif exam >= 60:
        print('D')
    else:
        print('F')