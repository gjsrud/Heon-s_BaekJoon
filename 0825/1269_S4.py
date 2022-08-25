#대칭 차집합 - 맵,집합

a,b = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

a_zip = set(a_list)
b_zip = set(b_list)

print(len(a_zip - b_zip)+len(b_zip - a_zip))