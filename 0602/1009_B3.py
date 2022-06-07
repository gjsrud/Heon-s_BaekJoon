t = int(input())
ans = []

for _ in range(t):
    a,b = map(str,input().split())
    b = int(b)
    one_list = []
    one_list.append(a)
    for i in range(b):
        num_a = int(a[-1])
        j = i+2
        ab = str(num_a**j)
        one = ab[-1]
        if one == a:
            break
        else:
            one_list.append(one)
    print(one_list)

    num = one_list[b%len(one_list)-1]
    ans.append(num)

print("\n".join(ans))


'''
2 2486
3 3971
4 46
5 5
6 6
7 7931
8 8426
9 91
'''