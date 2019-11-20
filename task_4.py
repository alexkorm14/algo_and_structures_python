"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

LEN_ROW = int(input('Введите длину ряда - '))
ELEMENT = 1
DENOMINATOR = -0.5

print('проверка по формуле сумме геометрической прогрессии - ',(ELEMENT*(DENOMINATOR**LEN_ROW-1))/(DENOMINATOR-1)) #---> проверка по формуле суммы геометрической прогрессии
if LEN_ROW==1:
	row_sum=ELEMENT
	
elif LEN_ROW>1:
	i=1
	row_sum = 1
	while i<LEN_ROW:
		ELEMENT*=DENOMINATOR
		row_sum+=ELEMENT
		i+=1
else:
	print('Число должно быть больше 0')
print(row_sum)
