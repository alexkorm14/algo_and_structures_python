import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 
"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу. 


-----> размерность матрицы 5 строк и 4 стобца. получается что заполняем 4 элемент строки суммой предыдущих элементов
"""

BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))

print()

MATRIX = []
for i in range(5):
	MATRIX.append(spisok(3,BEGIN_DIAPOSON,END_DIAPOSON))
for i in range(len(MATRIX)):
	sum_row = 0
	for j in range(len(MATRIX[i])):
		sum_row+=MATRIX[i][j]
	MATRIX[i].append(sum_row)

for i in range(len(MATRIX)):
	for j in range(len(MATRIX[i])):
		print(MATRIX[i][j], end=' ')
	print()



