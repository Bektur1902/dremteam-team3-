# Задание 3:
# a = 123
# b = 321
#  если сумма a и b четное -> вывести на экран половину суммы a и b
#  если половина суммы меньше b и больше a -> вывести на экран "b > sum/2 > a"

a = 123
b = 321

if (a + b) % 2 == 0:
	print((a + b)/2)
	if (a + b)/2 < b and (a + b)/2 > a:
		print('b > sum/2 > a') 