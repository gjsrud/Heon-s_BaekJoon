# 서로 다른 부분 문자열의 개수 

a = input()
ans = set()


for i in range(len(a)):
    for k in range(i,len(a)):
        ans.add(a[i:k+1])

print(len(ans))