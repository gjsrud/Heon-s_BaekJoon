a = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0

for i in range(len(a)):
    for k in range(len(cro)):
        if i+1 == len(a):
            break
        elif cro[k] == a[i] + a[i+1]:
            #print(cro[k],a[i]+a[i+1])
            count+=1
            break
    for j in range(len(cro)):
        if i+3 == len(a):
            break
        elif cro[k] == a[i] + a[i+1] + a[i+2]:
                count+=1
                break

print(len(a)-count)