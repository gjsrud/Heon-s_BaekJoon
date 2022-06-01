'''
(0,h)                       (w,h)
                    (x,y)

(0,0)                       (w,0)
'''

x,y,w,h = map(int,input().split())

ans = min(x,y,w-x,h-y)

print(ans)