one = int(input())
two = input()

a = []
for i in str(two):
    a.append(i)

a.reverse()

for j in a:
    print(one*int(j))
print(one*int(two))