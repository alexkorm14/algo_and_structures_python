
'''
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
'''
NUMBS_IN_ROW = int(input('сколько чисел в последовательности - ', ))
QUANTITY_IN_ROW = int(input('Введите число, которому надо посчитать количество встреч - ', ))
i=0
for m in range(1,NUMBS_IN_ROW+1):
	numb = int(input(f'Число {m}:  ',))
	while numb>=1:
		if numb%10==QUANTITY_IN_ROW:
			i+=1
		numb//=10

print(f'Число {QUANTITY_IN_ROW} встречается ровно {i} раза в последовательности')