a,b = map(int,input().split())
if a < -10000 or b > 10000:
    print("숫자가 잘못되었습니다.")
else: 
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")
