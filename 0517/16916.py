s = input()
p = input()
flag = False

for j in range(len(s)):
    if len(p)==1:
        print('0')
        flag=True
        break
    elif p==s[j:j+len(p)]:
        print('1')
        flag=True
        break

if flag==False:
    print('0')