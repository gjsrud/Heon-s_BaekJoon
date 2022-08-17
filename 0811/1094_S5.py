#막대기 - 비트마스킹

x = int(input())
stick = [64]

while True:
    if sum(stick) == x:
        print(len(stick))
        break
    if sum(stick) > x:
        temp = stick.index(min(stick))
        s = stick.pop(temp)
        s = s/2
        stick.append(s)
        if sum(stick) < x:
            stick.append(s)