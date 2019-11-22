import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 


# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
LEN_ROW = int(input('Введите длину последовательности - '))
DIVISIBLE = [i for i in range(2,10)]
NUMB_ROW = spisok(LEN_ROW, 2,100)
COUNT = []
print(NUMB_ROW)
print()
for i in DIVISIBLE:
	count_i = 0
	for numb in NUMB_ROW:
		if numb%i == 0:
			count_i+=1
	if count_i == 0:
		quantity_of_numb_divided_by_i = f'на число {i} делится {count_i} числел из диапозона'
	elif count_i == 1:
		quantity_of_numb_divided_by_i = f'на число {i} делится {count_i} число из диапозона'
	else:
		quantity_of_numb_divided_by_i = f'на число {i} делится {count_i} числа из диапозона'

	COUNT.append(quantity_of_numb_divided_by_i)
for el in COUNT:
	print(el)