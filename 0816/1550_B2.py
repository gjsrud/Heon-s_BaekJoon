#16진수

x = input()
sixteen = []
ten = 0

for i in reversed(range(len(x))):
    if ord(x[i]) < 65:
        sixteen.append(int(x[i]))
    elif ord(x[i]) == 65:
        sixteen.append(10)
    elif ord(x[i]) == 66:
        sixteen.append(11)
    elif ord(x[i]) == 67:
        sixteen.append(12)
    elif ord(x[i]) == 68:
        sixteen.append(13)
    elif ord(x[i]) == 69:
        sixteen.append(14)
    elif ord(x[i]) == 70:
        sixteen.append(15)

for k in range(len(sixteen)):
    a = sixteen[k]*16**k
    ten += a

print(ten)