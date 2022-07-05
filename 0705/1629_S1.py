#곱셈 - 분할 정복

'''
지수를 나누어 준다
만약 2^10은
2^5 * 2^5가 가능
2^11은
2^5 * 2^5 * 2가 가능
'''

a,b,c = map(int,input().split())

def DAC(a,b):
    if b == 1:
        return a%c
        
    dev = DAC(a, b//2)

    if b%2 == 0:
        return dev*dev%c
    else:
        return dev*dev*a%c
    

print(DAC(a,b))