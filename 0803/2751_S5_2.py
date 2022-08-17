import sys

N = int(sys.stdin.readline())
_list = []

for _ in range(N):
    _list.append(int(sys.stdin.readline()))

_list.sort()

for data in _list:
    print(data)
