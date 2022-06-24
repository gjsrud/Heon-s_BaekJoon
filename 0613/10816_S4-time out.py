#숫자카드2 - 집합과 맵 / 이분탐색

from sys import stdin


n = int(stdin.readline())
sang = list(map(int,stdin.readline().rstrip().split()))
sang.sort()
m = int(stdin.readline())
card = list(map(int,stdin.readline().rstrip().split()))
ans = []

for k in range(len(card)):
    first = 0
    last = len(sang)-1
    count = 0
    while True:
            mid = int((first + last) // 2)
            if sang[mid] == card[k]:
                count+=1
                p_mid = mid+1
                m_mid = mid-1
                while p_mid<=n-1 and card[k]==sang[p_mid]:
                    count+=1
                    p_mid+=1
                while m_mid>=0 and card[k]==sang[m_mid]:
                    count+=1
                    m_mid-=1
                ans.append(count)
                break
            elif sang[mid] > card[k]:
                last = mid - 1
            else:
                first = mid + 1
            if first > last:
                ans.append(count)
                break

print(*ans,sep=' ')