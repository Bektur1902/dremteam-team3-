num = '4729461084'
num = int(num)
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)