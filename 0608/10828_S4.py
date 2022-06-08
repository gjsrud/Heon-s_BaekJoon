n = int(input())
stack = []
ans = []

for _ in range(n):
    order = input()
    if order == 'pop':
        if len(stack) == 0:
            ans.append('-1')
        else:
            ans.append(stack[-1])
            stack.pop(-1)
    elif order == 'size':
        ans.append(str(len(stack)))
    elif order == 'empty':
        if len(stack) == 0:
            ans.append('1')
        else:
            ans.append('0')
    elif order == 'top':
        if len(stack) == 0:
            ans.append('-1')
        else:
            ans.append(stack[-1])
    else:
        stack.append(order[5:]) #뒤로 쌓인다


print('\n'.join(ans))