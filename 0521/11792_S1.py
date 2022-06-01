n = int(input())

'''
재귀함수 움직이는거 이해하고 싶으면 여기로
https://www.youtube.com/watch?v=FYCGV6F1NuY&t=363s
'''


def hanoi(n,pole1,pole2,pole3):
    if n==1:
        print(pole1,pole3)
    else:
        hanoi(n-1,pole1,pole3,pole2) 
        print(pole1,pole3)
        hanoi(n-1,pole2,pole1,pole3)

print(2**n-1)
hanoi(n,1,2,3)