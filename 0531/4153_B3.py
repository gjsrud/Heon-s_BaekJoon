ans = []

while True:
    list = []
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    else: 
        list= [a,b,c]
        list.sort()
        #print(list)
        if list[2]**2 == list[1]**2 + list[0]**2:
            ans.append("right")
        else:
            ans.append("wrong")

print("\n".join(i for i in ans))
