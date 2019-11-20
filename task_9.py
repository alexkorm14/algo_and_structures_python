"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

NUMBS_ROW = int(input('сколько чисел в последовательности - ', ))

i=0
max_count = 0
for m in range(1,NUMBS_ROW+1):
	count = 0
	numb = int(input(f'Число {m}:  ',))
	numb_for_operation=numb
	while numb_for_operation>1:
		count+=numb_for_operation%10
		numb_for_operation//=10 
		i+=1
	if count>max_count:
		max_count=count
		needed_numb = numb
print(f'Получилось число - {needed_numb} и сумма его цифр равна {max_count}')

