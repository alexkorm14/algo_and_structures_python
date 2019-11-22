import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 
# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
N = int(input('Введитие количество строк матрицы - ', ))
M = int(input('Введитие количество столбцов матрицы - ', ))

print()

BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))

print()


MATRIX = []
for i in range(N):
	MATRIX.append(spisok(M,BEGIN_DIAPOSON,END_DIAPOSON))
MIN_NUMB_COLUMN = []
i=0

for j in range(M):
	min_numb = MATRIX[i][0]
	for i in range(N):
		if MATRIX[i][j]<min_numb:
			min_numb = MATRIX[i][j]

	MIN_NUMB_COLUMN.append(min_numb)
print(MIN_NUMB_COLUMN)

for i in range(len(MATRIX)):
	for j in range(len(MATRIX[i])):
		print(MATRIX[i][j], end=' ')
	print()

MAX_IN_MIN = MIN_NUMB_COLUMN[0]
for i in range(len(MIN_NUMB_COLUMN)):
	if MIN_NUMB_COLUMN[i]>=MAX_IN_MIN:
		MAX_IN_MIN = MIN_NUMB_COLUMN[i]
print('Ответ - ', MAX_IN_MIN)
