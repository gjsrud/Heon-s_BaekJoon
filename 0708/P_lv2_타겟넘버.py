#DFS,BFS

def BFS(num,tar):
    
    ans = 0
    leave = [0]

    for i in num:
        tmp = []
        for k in leave:
            tmp.append(k + i)
            tmp.append(k - i)
        leave = tmp
    for h in leave:
        if h == tar:
            ans += 1
    
    return ans
    
print(BFS([1, 1, 1, 1, 1],3))
