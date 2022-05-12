a = int(input())
b = int(input())
c = []

for i in str(b):
    c.append(i)

c = map(int,c)

print(sum(c))