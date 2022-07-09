def solution(progresses, speeds):
    del_list = []
    answer = []
    cnt = 0
    a = [progresses[i]+speeds[i] for i in range(len(progresses))]

    while a:
        a = [a[i]+speeds[i] for i in range(len(a))]
        if a[0] >= 100:
            for i in range(len(a)):
                if a[i] >= 100:
                    del_list.append(i)
                    cnt+=1
                elif a[i] < 100:
                    break
                    
            for k in reversed(del_list):
                del a[k]
                del speeds[k]
            del_list = []
            answer.append(cnt)
            cnt = 0
        else:
            continue

    
    return answer
