a = list(range(1,10001))
b=[]

for i in range(1,10000):
    if i < 100:
        b.append(i//10 + i%10 + i)
    elif i <1000:
        x = i//100 + ((i%100)//10) + i%10 + i
        b.append(x)
    else :
        b.append(i//1000 + ((i%1000)//100) + ((i%100)//10) + i%10 + i)

c = list(set(a) - set(b))
c.sort()

for k in range(len(c)):
    print(c[k])

