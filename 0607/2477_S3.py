k = int(input())

ew = []
ns = []
all_leng = []

for i in range(6):

    d,l = map(int,input().split())
    all_leng.append(l)
    if d == 1 or d == 2:
        ew.append(l)
    else:
        ns.append(l)

a = max(ew)
b = max(ns)

a_in = all_leng.index(a)
b_in = all_leng.index(b)


if a_in != 5 and b_in != 5:
    s_length = abs(all_leng[a_in-1]-all_leng[a_in+1])
    s_width = abs(all_leng[b_in-1]-all_leng[b_in+1])
elif a_in == 5 and b_in != 5:
    s_length = abs(all_leng[0]-all_leng[4])
    s_width = abs(all_leng[b_in-1]-all_leng[b_in+1])
elif a_in != 5 and b_in == 5:
    s_length = abs(all_leng[a_in-1]-all_leng[a_in+1])
    s_width = abs(all_leng[0]-all_leng[4])


'''
1,2 중 최고 -> 양 옆은 세로줄임
옆의 세로줄에서 큰값 - 작은값 == 작은 사각형의 세로
3,4 중 최고 -> 양 옆은 가로줄
옆의 가로줄에서 큰값 - 작은값 == 작은 사각형의 가로
'''

b_square = a*b #큰 사각형 구하기
s_square = s_length*s_width

ans = (b_square-s_square)*k

print(ans)



