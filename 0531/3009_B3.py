'''
(5,7)       ()


(5,5)       (7,5)

만약에 
'''
x_list = []
y_list = []

for _ in range(3):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

#한 개인것만 가져오기
#-> 리스트에서 2개인것 지우기 => 이중 for문 써야하고 복잡
#count쓰면 1개인것만 가져올 수 있다

for i in range(3):
    if x_list.count(x_list[i])==1:
        x_ans = x_list[i]
    if y_list.count(y_list[i])==1:
        y_ans = y_list[i]

print(x_ans,y_ans)
    
