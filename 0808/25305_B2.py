from sys import stdin

input = stdin.readline

n,k = map(int,input().split())

num = list(map(int,input().split()))

num.sort(reverse=True)

print(num[k-1])