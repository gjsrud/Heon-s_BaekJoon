n = int(input())

a = n

count = 0

while True:
    b = a//10
    c = a%10
    d = (b+c) % 10
    e = c*10 + d
    count += 1
    if n == e :
        break
    a=e


print(count)
