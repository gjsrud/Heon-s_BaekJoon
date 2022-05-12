s = input()
list_s = list(s)
a_z = []
ans = []

for i in range(97,123):
    a_z.append(chr(i))

for k in a_z:
    count = 0
    check = 0
    for j in list_s:
        if k == j:
            ans.append(count)
            check=1
            break
        count+=1
    if check==0:
        ans.append(-1)

#이거 개좋네 ㅋㅋㅋㅋ
#print(*리스트 이름) -> 리스트를 한줄에 출력해 줌
print(*ans)
