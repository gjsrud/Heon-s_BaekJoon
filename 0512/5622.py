a = input()
count = 0

for i in range(len(a)):
    if ord(a[i]) > 64 and ord(a[i]) < 68:
        count += 3
    elif ord(a[i]) < 71:
        count += 4
    elif ord(a[i]) < 74:
        count += 5
    elif ord(a[i]) < 77:
        count += 6
    elif ord(a[i]) < 80:
        count += 7
    elif ord(a[i]) < 84:
        count += 8
    elif ord(a[i]) < 87:
        count += 9
    elif ord(a[i]) < 91:
        count += 10

print(count)