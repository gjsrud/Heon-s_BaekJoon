a = int(input())
count = a

for _ in range(a):
    x = input()
    flag = False
    for k in range(len(x)):
        if k+1 == len(x):
            break
        if x[k]!=x[k+1]:
            for i in range(k+2,len(x)):
                if x[k] == x[i]:
                    count-=1
                    flag=True #flagㅠㅠㅠㅠㅠ 유용하겠다 
                    break
                else:
                    continue
        if flag:
            break

print(count)
