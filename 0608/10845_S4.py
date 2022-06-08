n = int(input())
qu = []
ans = []

for _ in range(n):
    order = input()
    if order == 'pop':
        if len(qu) == 0:
            ans.append('-1')
        else:
            ans.append(qu[0])
            qu.pop(0)
    elif order == 'size':
        ans.append(str(len(qu)))
    elif order == 'empty':
        if len(qu) == 0:
            ans.append('1')
        else:
            ans.append('0')
    elif order == 'front': #[0]
        if len(qu) == 0:
            ans.append('-1')
        else:
            ans.append(qu[0])
    elif order == 'back': #[-1]
        if len(qu) == 0:
            ans.append('-1')
        else:
            ans.append(qu[-1])
    else:
        qu.append(order[5:]) #뒤로 쌓인다


print('\n'.join(ans))