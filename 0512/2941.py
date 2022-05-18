a = input()
cro = ['c=','c-','d-','lj','nj','s=','z=']
count = len(a)

'''
먼저 if문으로 0:3해서 dz=을 찾아주고 아니라면 다시 if
해서 일반문자 vs 크로아티아
지금하는거 nljj일때 nlj로 dz=검사
nl로 

'''

for i in range(count):
    #print(a[i:i+2],count)
    if a[i:i+3] == 'dz=':
        count -= 1
    else:
        for k in range(len(cro)):
            #print(a[i:i+2],count)
            if a[i:i+2] == cro[k]:
                count -= 1   

print(count)
