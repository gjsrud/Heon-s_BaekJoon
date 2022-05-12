num1,num2 = map(str,input().split())
num1, num2 = list(num1), list(num2)

num1.reverse()
num2.reverse()

sum_one = (num1[0]+num1[1]+num1[2])
sum_two = (num2[0]+num2[1]+num2[2])

a = int(sum_one)
b = int(sum_two)

print(max(a,b))

